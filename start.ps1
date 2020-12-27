
$file = 'Podrum.pyz'
$depsURL = 'https://raw.githubusercontent.com/Podrum/Podrum/master/requirements.txt'

function A-Start {
    if (Is-First-Launch) {
        First-Launch
    }
    Activate-Venv
    if (Is-Dev) {
        python .\src\__main__.py
    } else {
        python -O $file
    }
}
function Create-Venv {
    if (!(Test-Path '.\venv')){
        python -m venv venv
    }
}
function Is-First-Launch {
    return !(Test-Path '.\venv')
}
function Is-Dev {
    return !(Test-Path $file -PathType Leaf)
}
function Activate-Venv {
    .\venv\Scripts\Activate.ps1
}
function First-Launch {
    Write-Output 'First launch, creating venv...'
    Create-Venv
    Activate-Venv

    Write-Output 'Installing dependencies...'
    wget $depsURL -outfile ".\tmp-requirements.txt"
    pip install -r tmp-requirements.txt
    Remove-Item '.\tmp-requirements.txt'
}
A-Start
