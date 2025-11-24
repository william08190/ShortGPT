# ShortGPT 本地部署脚本
# 运行此脚本将在本地启动ShortGPT

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ShortGPT 本地部署脚本" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查Python
Write-Host "[1/4] 检查Python环境..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "[ERROR] 未找到Python，请先安装Python 3.10+" -ForegroundColor Red
    exit 1
}

# 检查.env文件
Write-Host ""
Write-Host "[2/4] 检查配置文件..." -ForegroundColor Yellow
$envPath = Join-Path $PSScriptRoot ".env"
if (Test-Path $envPath) {
    Write-Host "[OK] .env 配置文件已存在" -ForegroundColor Green

    # 显示配置摘要
    Write-Host ""
    Write-Host "当前配置:" -ForegroundColor Cyan
    $envContent = Get-Content $envPath
    foreach ($line in $envContent) {
        if ($line -match "^([A-Z_]+)=(.+)$") {
            $key = $matches[1]
            $value = $matches[2]
            if ($value.Length -gt 20 -and $key -match "KEY") {
                $maskedValue = $value.Substring(0, 10) + "..." + $value.Substring($value.Length - 5)
                Write-Host "  $key = $maskedValue" -ForegroundColor Gray
            } elseif ($value) {
                Write-Host "  $key = $value" -ForegroundColor Gray
            }
        }
    }
} else {
    Write-Host "[ERROR] 未找到 .env 配置文件" -ForegroundColor Red
    exit 1
}

# 加载环境变量
Write-Host ""
Write-Host "[3/4] 加载环境变量..." -ForegroundColor Yellow
Get-Content $envPath | ForEach-Object {
    if ($_ -match "^([^#][A-Z_]+)=(.*)$") {
        $name = $matches[1].Trim()
        $value = $matches[2].Trim()
        if ($value) {
            [System.Environment]::SetEnvironmentVariable($name, $value, "Process")
            Write-Host "  已设置: $name" -ForegroundColor Gray
        }
    }
}
Write-Host "[OK] 环境变量已加载" -ForegroundColor Green

# 启动ShortGPT
Write-Host ""
Write-Host "[4/4] 启动ShortGPT..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ShortGPT 正在启动..." -ForegroundColor Cyan
Write-Host "Web界面: http://localhost:31415" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "按 Ctrl+C 停止服务" -ForegroundColor Yellow
Write-Host ""

Set-Location $PSScriptRoot
python runShortGPT.py
