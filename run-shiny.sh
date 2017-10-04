#!/bin/bash

cd shiny
R -e "shiny::runApp(port=8100)"