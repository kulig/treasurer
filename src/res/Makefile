.PHONY: clean all

include files.mk

############################################################
# Определение платформозависимых штук
############################################################

PYUIC = pyside2-uic
PYRCC = pyside2-rcc
RM = rm -f
TARGET_DIR = ../ui/auto

############################################################
# Ниже этой строки не редактировать, если не понимаете,
# что делаете
############################################################

COMPILED_UI = $(UI_FILES:%.ui=$(TARGET_DIR)/%_ui.py)
COMPILED_RC = $(RC_FILES:%.qrc=$(TARGET_DIR)/%_rc.py)

all: res ui

res: $(COMPILED_RC)

ui: $(COMPILED_UI)

$(TARGET_DIR)/%_rc.py: %.qrc
	$(PYRCC) $< -o $@

$(TARGET_DIR)/%_ui.py: %.ui
	$(PYUIC) $< -o $@

clean:
	$(RM) $(COMPILED_UI) $(COMPILED_RC) $(COMPILED_UI:.py=.pyc) $(COMPILED_RC:.py=.pyc)
