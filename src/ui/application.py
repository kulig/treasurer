__version__ = u'0.0.1'


from PySide2 import QtWidgets

from ui import constants

QtWidgets.QApplication()
QtWidgets.QApplication.setOrganizationName(constants.APP_CODE)
QtWidgets.QApplication.setApplicationName(constants.APP_CODE)
QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(constants.QTSTYLE))
