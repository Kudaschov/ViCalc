from PySide6.QtWidgets import QPushButton, QMessageBox
from PySide6.QtGui import QFont, QPainter, QColor, QPaintEvent, QPen, QMouseEvent, QPixmap
from PySide6.QtCore import Qt, QRect, QPoint, QMargins
from ..CalcOperations import CalcOperations
from ..AppGlobals import AppGlobals

class CalcButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("", parent)
        self.row = -1 # row in keyboard grid
        self.column = -1 # column in keyboard grid
        self.norm_width = 1 # ratio: width to with of norm (usual) key

        self.shift_text = ""
        self._shift = False # shift key not pressed
        self.ctrl_text = ""
        self._ctrl = False # ctrl key is not pressed

        self.y_shift_area = 2 # from here starts the shift text
        self.height_shift_area = 18

        self.mouse_pos = None
        self.setMouseTracking(True)  # needed to get mouseMoveEvent without clicking

        self.bg_color = QColor("#FAFAFA") # background color for special cases like C and AC buttons

        self.corner_radius = 3 # button corner radius

        # default text alignment, if it differs from this, then use instead
        # only shift or ctrl rect both of them shift_and_ctrl_rect
        # that is useful for long text
        self.shift_text_default_alignment = Qt.AlignHCenter
        self.ctrl_text_default_alignment = Qt.AlignHCenter
        self.shift_text_alignment = self.shift_text_default_alignment
        self.ctrl_text_alignment = self.ctrl_text_default_alignment
        self.original_keyboard_text = "" # hint on top bottom

        # Apply stylesheet for hover/pressed states and to remove default borders/outlines
        self.setStyleSheet("""
            CalcButton {
                border: none;
                outline: none; /* Removes the dotted focus rectangle */
            }
            CalcButton:hover {
                background-color: #CCCCCC;
            }
            CalcButton:pressed {
                background-color: #BBBBBB;
            }
        """)

        self.text_font = QFont("Helvetica", 10)
        self.text_highlight_font = QFont("Helvetica", 10, QFont.Bold)
        self.text_color = QColor("black")
        self.shift_font = QFont("Helvetica", 10)
        self.shift_highlight_font = QFont("Helvetica", 10, QFont.Bold)
        self.shift_color = QColor("#0000A0")
        self.shift_highlight_color = QColor("#0000FF")
        self.ctrl_font = QFont("Helvetica", 10)
        self.ctrl_highlight_font = QFont("Helvetica", 10, QFont.Bold)
        self.ctrl_color = QColor("#009000")
        self.ctrl_highlight_color = QColor("#00C000")
        self.original_keyboard_text_color = QColor("#606060")
        self.original_keyboard_text_font = QFont("Helvetica", 9)

        self.base_operation = CalcOperations.nop
        self.shift_operation = CalcOperations.nop
        self.ctrl_operation = CalcOperations.nop

        # self.setCursor(Qt.PointingHandCursor)
        self.clicked.connect(self._on_button_clicked)

    def _on_button_clicked(self):
        if AppGlobals.input_box != None:
            if (self.mouse_pos != None and self.shift_rect().contains(self.mouse_pos)):
                AppGlobals.input_box.button_clicked(self.shift_operation)
            elif (self.mouse_pos != None and self.ctrl_rect().contains(self.mouse_pos)):
                AppGlobals.input_box.button_clicked(self.ctrl_operation)
            else:
                AppGlobals.input_box.button_clicked(self.base_operation)
        else:
            QMessageBox.information(self, "Information", "No operation configured")

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing) # Keep anti-aliasing for smooth lines
        painter.save()

        # self.pixmap = QPixmap('ui/img/cube_root.png')
        # painter.drawPixmap(0, 0, self.pixmap)

        # Manual drawing of the button's background based on state
        current_bg_color = QColor("#F9F9F9") # Default background color
        bg_rect = self.rect().adjusted(0, self.height_shift_area, -1, -1)

        if self.isDown(): # Button is currently pressed
            current_bg_color = QColor("#BBBBBB")
        elif self.underMouse(): # Mouse is hovering over the button
            current_bg_color = QColor("#BEE6FD")
            painter.setBrush(current_bg_color)
            painter.setPen(Qt.NoPen)

            # mouse hovering round rect
            if self.shift_text != self.ctrl_text:
                # shift and ctrl text are not equal
                if ((len(self.shift_text) == 0 or len(self.ctrl_text) == 0) and
                    self.mouse_pos != None and self.shift_and_ctrl_rect().contains(self.mouse_pos)):
                    # one of texts is empty, use the whole rect
                    painter.drawRoundedRect(self.shift_and_ctrl_rect(), self.corner_radius, self.corner_radius)
                elif (self.mouse_pos != None and self.shift_rect().contains(self.mouse_pos)):
                    painter.drawRoundedRect(self.shift_rect(), self.corner_radius, self.corner_radius)
                elif (self.mouse_pos != None and self.ctrl_rect().contains(self.mouse_pos)):
                    painter.drawRoundedRect(self.ctrl_rect(), self.corner_radius, self.corner_radius)
                else:
#                    painter.fillRect(bg_rect, current_bg_color)
                    painter.drawRoundedRect(bg_rect, self.corner_radius, self.corner_radius)
            else:
                # shift and ctrl text is equal
                if (self.mouse_pos != None and self.shift_and_ctrl_rect().contains(self.mouse_pos)):
                    painter.drawRoundedRect(self.shift_and_ctrl_rect(), self.corner_radius, self.corner_radius)
                else:
                    painter.fillRect(bg_rect, current_bg_color)

        if self.shift_text != self.ctrl_text:
            # shift and ctrl text is different, draw both texts
            # Draw the shift text
            if self._shift:
                painter.setFont(self.shift_highlight_font)
                painter.setPen(self.shift_highlight_color)
            else:
                painter.setFont(self.shift_font)
                painter.setPen(self.shift_color)

            # draw text only, if it is different to button text or no shift is pressed
            # if shift is pressed show it anyway, e. g. case shift + V -> MR
            if self.text() != self.shift_text or self._shift == True:
                if self.shift_text_alignment == self.shift_text_default_alignment:
                    if len(self.ctrl_text) > 0:
                        # text is standard aligned
                        painter.drawText(self.shift_rect(), Qt.AlignHCenter | Qt.AlignTop, self.shift_text)
                    else: # no ctrl text, use the whole rect
                        painter.drawText(self.shift_and_ctrl_rect(), Qt.AlignHCenter | Qt.AlignTop, self.shift_text)
                else:
                    # text is big, try it to align in shift_and_ctrl_rect
                    painter.drawText(self.shift_and_ctrl_rect(), self.shift_text_alignment | Qt.AlignTop, self.shift_text)

            # Draw the ctrl text
            if self._ctrl:
                painter.setFont(self.ctrl_highlight_font)
                painter.setPen(self.ctrl_highlight_color)
            else:
                painter.setFont(self.ctrl_font)
                painter.setPen(self.ctrl_color)

            # draw text only, if it is different to button text
            if (self.text() != self.ctrl_text):
                if self.ctrl_text_alignment == self.ctrl_text_default_alignment:
                    if len(self.shift_text) > 0:
                        # text is standard aligned
                        painter.drawText(self.ctrl_rect(), self.ctrl_text_alignment | Qt.AlignTop, self.ctrl_text)
                    else: # no shift text, use the whole rect
                        painter.drawText(self.shift_and_ctrl_rect(), self.ctrl_text_alignment | Qt.AlignTop, self.ctrl_text)
                else:
                    # text is big, try it to align in shift_and_ctrl_rect
                    painter.drawText(self.shift_and_ctrl_rect(), self.ctrl_text_alignment | Qt.AlignTop, self.ctrl_text)
        else:
            # shift and ctrl text is the same
            # Draw the shift text on top middle
            if self._shift:
                painter.setFont(self.shift_highlight_font)
                painter.setPen(self.shift_highlight_color)
            elif self._ctrl:
                painter.setFont(self.ctrl_highlight_font)
                painter.setPen(self.ctrl_highlight_color)
            else:
                painter.setFont(self.shift_font)
                painter.setPen(self.shift_color)

            # draw text only, if it is different to button text
            if (self.text() != self.shift_text):
                painter.drawText(QRect(3, self.y_shift_area, self.width() - 6, 20), Qt.AlignTop | Qt.AlignHCenter, self.shift_text)


        # --- Draw the rectangle using drawRect() ---
        rect_y = self.height_shift_area 
        
        # Define the rectangle to draw
        rectangle_to_draw = QRect(1, rect_y, self.width() - 3, self.height() - rect_y - 1)

        if self.underMouse():
            # draw background
            painter.setPen(QPen(QColor("#C0C0C0"), 0, Qt.SolidLine))
            if (self.bg_color == None):
                painter.setBrush(Qt.NoBrush) # Ensures only the outline is drawn
            else:
                # mouse over shift and ctrl, set base background
                if (self.mouse_pos != None and self.shift_and_ctrl_rect().contains(self.mouse_pos)):
                    painter.setBrush(QColor(self.bg_color))
            painter.drawRoundedRect(rectangle_to_draw, self.corner_radius, self.corner_radius) # Draws the complete rectangle outline
        else:
            # draw background
#            painter.setPen(QPen(QColor("#707070"), 0, Qt.SolidLine))
            painter.setPen(QPen(QColor("#C0C0C0"), 0, Qt.SolidLine))
            if (self.bg_color == None):
                painter.setBrush(Qt.NoBrush) # Ensures only the outline is drawn
            else:
                painter.setBrush(QColor(self.bg_color))
            painter.drawRoundedRect(rectangle_to_draw, self.corner_radius, self.corner_radius) # Draws the complete rectangle outline

        # Draw the main centered text
        if (self._shift == False and self._ctrl == False):
            painter.setFont(self.text_highlight_font)
        else:
            painter.setFont(self.text_font)

        painter.setPen(self.text_color)
        painter.drawText(rectangle_to_draw, Qt.AlignCenter, self.text())

        # Draw original keyboard text
        if self.original_keyboard_text != self.text():
            painter.setFont(self.original_keyboard_text_font)
            painter.setPen(self.original_keyboard_text_color)
            painter.drawText(rectangle_to_draw.marginsRemoved(QMargins(0, 0, 2, 0)),
                Qt.AlignRight | Qt.AlignBottom, self.original_keyboard_text)

        painter.restore()

    @property
    def shift(self) -> bool:
        """Returns the current shift state of the button."""
        return self._shift
    
    @shift.setter
    def shift(self, state: bool):
        """
        Sets the shift state of the button and requests a repaint.
        """
        if self._shift != state:
            self._shift = state
            # Request an update to trigger paintEvent
            self.update() # <--- Key change here!

    @property
    def ctrl(self) -> bool:
        """Returns the current shift state of the button."""
        return self._ctrl
    
    @ctrl.setter
    def ctrl(self, state: bool):
        """
        Sets the shift state of the button and requests a repaint.
        """
        if self._ctrl != state:
            self._ctrl = state
            # Request an update to trigger paintEvent
            self.update() # <--- Key change here!

    def mouseMoveEvent(self, event: QMouseEvent):
        self.mouse_pos = event.position().toPoint()  # store local position
        self.update()  # trigger paintEvent
        super().mouseMoveEvent(event)

    def shift_rect(self):
        return QRect(0, 1, self.rect().width() / 2, self.height_shift_area)
    
    def ctrl_rect(self) -> QRect:
        rect = QRect(self.rect().width() / 2, 1, self.rect().width() / 2, self.height_shift_area)
        #rect = rect.adjusted(0, 0, -20, 0)
        return rect
    
    def shift_and_ctrl_rect(self) -> QRect:
        rect = QRect(0, 1, self.rect().width(), self.height_shift_area)
        rect = rect.adjusted(0, 0, -1, 0)
        return rect