import gradio as gr

from gui.content_automation_ui import GradioContentAutomationUI
from gui.ui_abstract_base import AbstractBaseUI
from gui.ui_components_html import GradioComponentsHTML
from gui.ui_tab_asset_library import AssetLibrary
from gui.ui_tab_config import ConfigUI
from gui.i18n import I18n
from shortGPT.utils.cli import CLI


class ShortGptUI(AbstractBaseUI):
    '''Class for the GUI. This class is responsible for creating the UI and launching the server.'''

    def __init__(self, colab=False):
        super().__init__(ui_name='gradio_shortgpt')
        self.colab = colab
        CLI.display_header()

    def create_interface(self):
        '''Create Gradio interface'''
        with gr.Blocks(theme=gr.themes.Default(spacing_size=gr.themes.sizes.spacing_sm), css="footer {visibility: hidden}", title="ShortGPT Demo") as shortGptUI:
            with gr.Row(variant='compact'):
                gr.HTML(GradioComponentsHTML.get_html_header())
                with gr.Column(scale=1, min_width=200):
                    language_switcher = gr.Radio([I18n.t("switch_to_chinese"), I18n.t("switch_to_english")],
                                                 label=I18n.t("language"),
                                                 value=I18n.t("switch_to_chinese") if I18n.current_lang == "zh" else I18n.t("switch_to_english"),
                                                 interactive=True)
                    language_info = gr.HTML("")

                    def change_language(lang_choice):
                        if lang_choice == "中文":
                            I18n.set_language("zh")
                            return "<p style='color: green; font-size: 12px;'>✓ 语言已切换到中文。请刷新页面查看完整效果。</p>"
                        else:
                            I18n.set_language("en")
                            return "<p style='color: green; font-size: 12px;'>✓ Language switched to English. Please refresh the page to see full effect.</p>"

                    language_switcher.change(change_language, [language_switcher], [language_info])

            self.content_automation = GradioContentAutomationUI(shortGptUI).create_ui()
            self.asset_library_ui = AssetLibrary().create_ui()
            self.config_ui = ConfigUI().create_ui()
        return shortGptUI

    def launch(self):
        '''Launch the server'''
        shortGptUI = self.create_interface()
        if not getattr(self, 'colab', False):
                    print("\n\n********************* STARTING SHORGPT **********************")
                    print("\nShortGPT is running here --> http://localhost:31415\n")
                    print("********************* STARTING SHORGPT **********************\n\n")
        shortGptUI.queue().launch(server_port=31415, height=1000, allowed_paths=["public/","videos/","fonts/"], share=self.colab, server_name="0.0.0.0")



if __name__ == "__main__":
    app = ShortGptUI()
    app.launch()


import signal

def signal_handler(sig, frame):
    print("Closing Gradio server...")
    import gradio as gr
    gr.close_all()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)