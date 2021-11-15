#! /bin/bash
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
chmod +x ./main_enhancement.py

# creating desktop icon

rm fp-enhancer.desktop
touch fp-enhancer.desktop

chmod +x fp-enhancer.desktop

echo fp-enhancer.desktop fue creado, puede acceder a la aplicacion haciendo doble click en fp-enhancer.desktop
echo [Desktop Entry] >> fp-enhancer.desktop
echo Version=0.0.1 >> fp-enhancer.desktop
echo Name=FingerPrintEnhancer >> fp-enhancer.desktop
echo Comment=Interfaz grafica para el mejorador de huellas digitales >> fp-enhancer.desktop
echo Exec=$(pwd)/finger-print-enhancer-gui >> fp-enhancer.desktop
echo Icon=$(pwd)/fpe-icon.jpg >> fp-enhancer.desktop
echo Terminal=false >> fp-enhancer.desktop 
echo Type=Application >> fp-enhancer.desktop
echo "Categories=Utility;Application;" >> fp-enhancer.desktop
