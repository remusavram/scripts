#-*-coding:utf-8-*-
"""
@package: tx_common.qt.widgets.confirmdialog
@brief: A PySide confirm dialog providing multiple ways of use.
@author: Paul Schweizer
@email: paul.schweizer@trixter.de
@copyright: 2014 TRIXTER Film GmbH
"""
__all__ = ['ConfirmDialog']
from PySide import QtCore, QtGui
from tx import path
from tx_common import qt
from tx_common.qt.widgets import txwindowheader


form_class, base_class = qt.utils.loadUiType(path.Path(__file__).dirname().dirname() /
                                             'resource' / 'confirmdialog.ui')


class ConfirmDialog(base_class, form_class):

    """This dialog can be used in three different ways:
        * floating: the dialog floats normally, no specific attributes or
                    styles are set, except that the dialog appears frameless
                    which should be implemented as the standard behavior for
                    all widgets.
                    The mode identifier for floating is 0
        * non-floating: the dialog is fixed to the center of the screen,
                        spanning the whole screen width. Furthermore, the
                        dialog is styled to fit with the companies colors and form
                        In fixed mode, also animation is possible. The dialog is
                        then being slid in from the left when opening and out to
                        left when closing.
                        The mode identifier for non-floating is 1
        * loading screen: when given a callback, the dialog acts as loading
                          screen, displaying the given message and title until
                          the callback has run. After that, the dialog is
                          automatically closed. Animations are disabled in
                          this mode.
                          The mode identifier for loading screen is 2

    """

    def __init__(self,
                 title='Confirm Dialog',
                 message=None,
                 button=['Confirm', 'Cancel'],
                 default_button='Confirm',
                 cancel_button='Cancel',
                 dismiss_string='Cancel',
                 floating=False,
                 animated=True,
                 inner_widget=None,
                 callback=None,
                 predefined_style=None,
                 size=None):
        """Initializes the ConfirmDialog.
        @param title: the title for the dialog
        @param message: the message to be displayed
        @param button: the buttons
        @param default_button: the preselected button
        @param cancel_button: the cancel button
        @param dismiss_string: the string used for canceling, not implemented
        @param floating: whether the confirm dialog is floating or fixed to the
                         center of the screen
        @param animated: whether the dialog is animated, animation only works in
                         non-floating mode
        @param inner_widget: a qt widget that is to be displayed in the
                             confirm dialog.
        @param callback: a callback that gets executed after the dialog has been
                         shown. The dialog is closed once the callback has run.
        @param predefined_style: the id for a predefined style for the confirm
                                 dialog.
        @param size: the size of the dialog
        @type title: string
        @type message: string
        @type button: list
        @type default_button: string
        @type cancel_button: string
        @type dismiss_string: string
        @type floating: boolean
        @type animated: boolean
        @type inner_widget: QWidget
        @type callback: function
        @type predefined_style: Integer
        @type size: list

        """
        super(ConfirmDialog, self).__init__()
        self.setupUi(self)
        self.status = False
        self._animation_speed = 100
        self._title = title
        self._message = message
        self._button = button
        self._default_button = default_button
        self._cancel_button = cancel_button
        self.focussed_button = None
        self._dismiss_string = dismiss_string
        self._floating = floating
        self._animated = animated
        self.inner_widget = inner_widget
        self._callback = callback
        self._predefined_style = predefined_style
        self.painted = False
        if size is not None:
            self.resize(size[0], size[1])
        # END if
        self._set_predefined_style()
        self._set_mode()
        self._setup_button()
        self._setup_ui()
        self._init_signals()
        self._show_dialog()
    # END def __init__

    def _set_mode(self):
        """Sets the mode according to the provided inputs."""
        if self._floating:
            self._mode = 0
        # END if
        if not self._floating:
            self._mode = 1
        # END if
        if self._callback is not None:
            self._mode = 2
            self._button = list()
        # END if
    # END def _set_mode

    def _set_predefined_style(self):
        """Sets the confirm dialog to one of the predefined styles.
        Available styles are:
        0: Information
        1: A Warning
        2: An Error message

        """
        if self._predefined_style == 0:
            self._button = ['OK']
            self._default_button = 'OK'
            self.predefined_style_lbl.setAccessibleName('information')
            css = ('background-color:#222822; color:#99cc99;')
            self.predefined_style_lbl.setStyleSheet(css)
            self.predefined_style_lbl.setText('Information')
        elif self._predefined_style == 1:
            self._button = ['OK']
            self._default_button = 'OK'
            css = ('background-color:#333322; color:#cccc99;')
            self.predefined_style_lbl.setStyleSheet(css)
            self.predefined_style_lbl.setText('Warning')
        elif self._predefined_style == 2:
            self._button = ['OK']
            self._default_button = 'OK'
            css = ('background-color:#332222; color:#99cccc;')
            self.predefined_style_lbl.setStyleSheet(css)
            self.predefined_style_lbl.setText('Error')
        else:
            self.predefined_style_lbl.hide()
        # END if
    # END def _set_predefined_style

    def _setup_ui(self):
        """Sets up the UI.
            * window title
            * message text
            * trixter header
            * stylesheet and geometry adjustments for non floating
            * adds the inner widget if any is given

        """
        self.maincontent_vlay.insertWidget(0, txwindowheader.TXWindowHeader(self._title))
        self.setWindowTitle(self._title)
        self.setWindowFlags(QtCore.Qt.Widget|QtCore.Qt.FramelessWindowHint)
        if self._message is not None:
            self.message_lbl.setText(self._message)
        else:
            self.message_lbl.hide()
        # END if
        if self._mode > 0:
            self.setGeometry(self._get_display_geometry())
            css_file = path.Path(__file__).dirname().dirname() / 'resource' / 'tx.css'
            with open(css_file, 'r') as f:
                css = f.read()
                f.close()
            # END with
            self.setStyleSheet(css)
            self.close_btn.hide()
            self.topbar_hlay.hide()
            self.layout().setContentsMargins(9, 25, 9, 25)

            self.background_wid.layout().insertSpacing(0, 40)
            self.background_wid.layout().insertSpacing(2, 40)
            self.main_wid.setMaximumWidth(600)
        # END if

        if self.inner_widget is not None:
            self.inner_widget.dialog = self
            self.inner_widget_vlay.addWidget(self.inner_widget)
        # END if
    # END def _setup_ui

    def _get_start_geometry(self):
        """Calculates the optimal geometry data for the confirm dialog in it's
        smallest form.
        @return: a QRect with the correct geometry data.

        """
        desktop = QtGui.QApplication.instance().desktop()
        available_geometry = desktop.screenGeometry(QtGui.QCursor().pos())
        x = available_geometry.x()
        y = (available_geometry.height()/2) - (self.height()/2)
        w = self.width()
        h = self.height()
        return QtCore.QRect(x, y, w, h)
    # END def _get_start_geometry

    def _get_display_geometry(self):
        """Calculates the optimal geometry data for the confirm dialog in it's
        final display appearance.
        @return: a QRect with the correct geometry data.

        """
        desktop = QtGui.QApplication.instance().desktop()
        available_geometry = desktop.screenGeometry(QtGui.QCursor().pos())
        x = available_geometry.x()
        y = (available_geometry.height()/2) - (self.height()/2)
        w = available_geometry.width()
        h = self.height()
        return QtCore.QRect(x, y, w, h)
    # END def _get_display_geometry

    def _get_end_geometry(self):
        """Calculates the optimal geometry data for the confirm dialog in it's
        final display appearance.
        @return: a QRect with the correct geometry data.

        """
        desktop = QtGui.QApplication.instance().desktop()
        available_geometry = desktop.screenGeometry(QtGui.QCursor().pos())
        x = available_geometry.x() + available_geometry.width()
        y = (available_geometry.height()/2) - (self.height()/2)
        w = 0
        h = self.height()
        return QtCore.QRect(x, y, w, h)
    # END def _get_end_geometry

    def _setup_button(self):
        """Sets up the buttons with the correct signals."""
        self._buttons = list()
        for i, button_name in enumerate(self._button):
            button = QtGui.QPushButton(button_name)
            self.actions_vlay.addWidget(button)
            if button_name == self._cancel_button:
                button.clicked.connect(self.cancel)
            else:
                button.clicked.connect(self.confirm)
            # END if
            self._buttons.append(button)
            if button_name == self._default_button:
                self._focus_button(i)
            # END if
        # END for
    # END def _setup_button

    def _focus_button(self, index):
        """Focuses the given button.
        @param index: the index of the focus button in the buttons list
        @type index: Integer

        """
        for i, button in enumerate(self._buttons):
            if i == index:
                button.setDefault(True)
                self.focussed_button = button
            else:
                button.setDefault(False)
            # END if
        # END for
    # END def _focus_button

    def _init_signals(self):
        """Initializes the signals."""
        self.close_btn.clicked.connect(self.close)
    # END def _init_widgets

    def keyPressEvent(self, event):
        """Integrates the following button signals into the ConfirmDialog:
            * arrow left/right: cycles through the buttons
            * enter: executes the currently selected button's click action if any
                     of the buttons has focus. If no button has focus and an
                     inner widget exists with a focussed button, that buttons
                     click event is being executed.
            * esc: aborts the confirm dialog by using the cancel action
        @param event: the key press event
        @type event: object
        @return: a standard keyPressEvent

        """
        key = event.key()
        next = 16777236
        prev = 16777234
        enter = 16777220
        esc = 16777216
        if key == next or key == prev:
            if self.focussed_button is None:
                index = -1
            else:
                index = self._buttons.index(self.focussed_button)
            # END if
            if key == next:
                new_index = index + 1
                if new_index >= len(self._buttons):
                    new_index = 0
                # END if
            else:
                new_index = index - 1
                if new_index < 0:
                    new_index = len(self._buttons)-1
                # END if
            # END if
            self._focus_button(new_index)
        elif key == enter:
            if self.focussed_button is not None:
                self.focussed_button.click()
            else:
                if self.inner_widget is not None:
                    if hasattr(self.inner_widget, 'focussed_button'):
                        if self.inner_widget.focussed_button is not None:
                            self.inner_widget.focussed_button.click()
                        # END if
                    # END if
                # END if
            # END if
        elif key == esc:
            self.cancel()
        # END if
        return QtGui.QWidget.keyPressEvent(self, event)
    # END def mousePressEvent

    def mousePressEvent(self, event):
        """The mouse press event captures the position of the press event, so the
        window can be moved relative to the cursor position,
        @param event: the move event
        @type event: object
        @return: a standard mousePressEvent

        """
        self.mouse_press_position = event.pos()
        return QtGui.QWidget.mousePressEvent(self, event)
    # END def mousePressEvent

    def mouseMoveEvent(self, event):
        """Moves the widget to the given location on the screen.
        Only active if floating is set to False.
        @param event: the move event
        @type event: object
        @return: a standard mouseMoveEvent

        """
        if self._floating:
            self.move(event.globalPos().x() - self.mouse_press_position.x(),
                      event.globalPos().y() - self.mouse_press_position.y())
        # END if
        return QtGui.QWidget.mouseMoveEvent(self, event)
    # END def mousePressEvent

    def confirm(self):
        """Confirms and closes the dialog. The status is set to True.
        If the dialog is animated, the end animation is started.

        """
        self.status = True
        if self._mode == 1:
            try:
                self._end_animation()
            except Exception as err:
                print err
                self.close()
            # END try
        else:
            self.close()
        # END if
    # END def confirm

    def cancel(self):
        """Cancels and closes the dialog. The status is set to False.
        If the dialog is animated, the end animation is started.

        """
        self.status = False
        if self._mode == 1:
            try:
                self._end_animation()
            except Exception as err:
                print err
                self.close()
            # END try
        else:
            self.close()
        # END if
    # END def cancel

    def _start_animation(self):
        """Executes the start animation to slide the dialog in from the left."""
        self.start_anim = QtCore.QPropertyAnimation(self, 'geometry')
        self.start_anim.setDuration(self._animation_speed)
        self.start_anim.setStartValue(self._get_start_geometry())
        self.start_anim.setEndValue(self._get_display_geometry())
        self.start_anim.start()
    # END def _start_animation

    def _end_animation(self):
        """Executes the end animation to slide the dialog out to the right."""
        self.end_anim = QtCore.QPropertyAnimation(self, 'geometry')
        self.end_anim.setDuration(self._animation_speed)
        self.end_anim.setStartValue(self.geometry())
        self.end_anim.setEndValue(self._get_end_geometry())
        self.end_anim.finished.connect(self.close)
        self.end_anim.start()
    # END def _end_animation

    def _show_dialog(self):
        """Shows the dialog."""
        self.exec_()
    # END def _show_dialog

    def showEvent(self, event):
        """Executes the start animation if dialog is animated and non-floating.
        @param event: the show event
        @type event: object
        @return: a standard showEvent

        """
        if self._mode == 1:
            self._start_animation()
        # END if
        return QtGui.QWidget.showEvent(self, event)
    # END def showEvent

    def paintEvent(self, event):
        """The paint event for the confirm dialog.
        Hijacked to provide the possibility to display this confirm dialog until
        the callback has been executed.
        If no callback is set, a standard QPaintEvent is returned.
        @param event: the QPaintEvent
        @return: a standard QPaintEvent

        """
        if self._mode != 2:
            return QtGui.QPaintEvent(self.rect())
        elif self.painted == False:
            self.painted = True
            cursor = QtGui.QCursor()
            cursor.setShape(QtCore.Qt.WaitCursor)
            self.setCursor(cursor)
            self.update(self.rect())
        elif self.painted:
            try:
                self._callback()
                self.confirm()
            except:
                self.cancel()
            # END try
        # END if
    # END def paintEvent
# END class ConfirmDialog
