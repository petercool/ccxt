<?php

namespace ccxt\async;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import

class binanceusdm extends binance {

    public function describe() {
        return $this->deep_extend(parent::describe (), array(
            'id' => 'binanceusdm',
            'name' => 'Binance USDⓈ-M',
            'urls' => array(
                'logo' => 'https://user-images.githubusercontent.com/1294454/117738721-668c8d80-b205-11eb-8c49-3fad84c4a07f.jpg',
            ),
            'options' => array(
                'defaultType' => 'future',
            ),
        ));
    }
}
