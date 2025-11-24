@echo off
chcp 65001 >nul
echo ========================================
echo ShortGPT 本地部署启动器
echo ========================================
echo.

cd /d %~dp0

echo [1/3] 加载环境变量...
for /f "tokens=1,2 delims==" %%a in (.env) do (
    if not "%%a"=="" if not "%%a:~0,1%"=="#" (
        set "%%a=%%b"
        echo   已设置: %%a
    )
)
echo.

echo [2/3] 检查依赖...
python -c "import gradio; import openai; print('OK')" 2>nul
if errorlevel 1 (
    echo [WARN] 缺少依赖，正在安装...
    pip install -r requirements.txt
)
echo.

echo [3/3] 启动ShortGPT...
echo ========================================
echo Web界面: http://localhost:31415
echo 按 Ctrl+C 停止服务
echo ========================================
echo.

python runShortGPT.py

pause
