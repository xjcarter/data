#!/bin/bash

python yahoo_data.py "^GSPC" "^NDX" "^RUT" "^DJI" SPY DIA IVV IWM UPRO UDOW TQQQ QQQ SSO
python data_catalog.py "^GSPC" "^NDX" "^RUT" "^DJI" SPY DIA IVV IWM UPRO UDOW TQQQ QQQ SSO
