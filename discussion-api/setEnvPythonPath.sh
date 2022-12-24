#!/bin/sh

# Black        0;30     Dark Gray     1;30
# Red          0;31     Light Red     1;31
# Green        0;32     Light Green   1;32
# Brown/Orange 0;33     Yellow        1;33
# Blue         0;34     Light Blue    1;34
# Purple       0;35     Light Purple  1;35
# Cyan         0;36     Light Cyan    1;36
# Light Gray   0;37     White         1;37

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}This Script will help you to set permanently your ${YELLOW}PYTHONPATH${BLUE}\nvariables for this app appending a Pythonpath to your ~/.bashrc.${NC}";
while true; do
    read -p "Are you positioned in you app's root folder? [y/n]: " yn
    case $yn in
        [Yy]* ) 
            echo "Setting PYTHONPATH for this app";
            # Exporting app directory
            echo "export PYTHONPATH=$PWD" >> ~/.bashrc;
            cd ..
            # Exporting parent directory
            echo "export PYTHONPATH=$PWD" >> ~/.bashrc;

            echo -e "${GREEN}Export finished, permanent variables implemented.${NC}";
            break;;
        [Nn]* ) 
            echo -e "${YELLOW}Please run this script in your app's root folder.${NC}"; exit;;
        * ) echo -e "${YELLOW}Please answer yes or no.${NC}";;
    esac
done
