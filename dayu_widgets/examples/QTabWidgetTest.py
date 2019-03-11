#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MMessage import MMessage
from dayu_widgets.MTabWidget import MTabWidget
from dayu_widgets.qt import *


class QTabWidgetTest(QWidget):
    def __init__(self, parent=None):
        super(QTabWidgetTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        class_list = [MTabWidget]
        for cls in class_list:
            tab_line = cls(parent=self)
            tab_line.set_type('line')
            tab_line.addTab(MLabel('test 1'), u'标签一')
            tab_line.addTab(MLabel('test 2'), u'标签二')
            tab_line.addTab(MLabel('test 3'), u'标签三')

            tab_card = cls()
            tab_card.set_type('card')
            tab_card.addTab(MLabel('test 1'), u'标签一 ttt')
            tab_card.addTab(MLabel('test 2'), u'标签二 ttt')
            tab_card.addTab(MLabel('test 3'), u'标签三 ttt')

            self.tab_closable = cls()
            self.tab_closable.set_type('card')
            self.tab_closable.setTabsClosable(True)
            self.tab_closable.addTab(MLabel('test 1'), u'标签一 ttt')
            self.tab_closable.addTab(MLabel('test 2'), u'标签二 ttt')
            self.tab_closable.addTab(MLabel('test 3'), u'标签三 ttt')
            self.tab_closable.tabCloseRequested.connect(self.slot_close_tab)

            lay = QVBoxLayout()
            lay.addWidget(tab_line)
            lay.addWidget(tab_card)
            lay.addWidget(self.tab_closable)
            main_lay.addLayout(lay)

        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_close_tab(self, index):
        if index > 0:
            self.tab_closable.removeTab(index)
            MMessage.info({'content': u'成功关闭一个标签',
                           'closable': True
                           }, parent=self)
        else:
            MMessage.warning({'content': u'请不要关闭第一个标签',
                              'closable': True
                              }, parent=self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = QTabWidgetTest()
    test.show()
    sys.exit(app.exec_())