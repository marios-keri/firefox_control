import pyautogui as pyauto

class Search():
    """Search commands for firefox"""
    def __init__(self):
        self.SearchKeyword = pyauto

    @staticmethod
    def find(self):
        """find in the document"""
        self.SearchKeyword.hotkey('Ctrl', 'F')

    @staticmethod
    def find_again(self):
        """Find Again"""
        self.SearchKeyword.hotkey('F3')

    @staticmethod
    def find_previous(self):
        """Find Previous"""
        self.SearchKeyword.hotkey('Shift', 'F3')
 
    @staticmethod
    def quick_find_within_link_text(self):
        """Quick Find within link-text only"""
        self.SearchKeyword.hotkey("'")
   
    @staticmethod
    def quick_find(self):
        """Quick Find"""
        self.SearchKeyword.hotkey('/')

    @staticmethod
    def close_find(self):
        """Close the Find or Quick Find bar"""
        self.SearchKeyword.hotkey('Esc')

    @staticmethod
    def focus_search_bar(self):
        """Focus Search bar"""
        self.SearchKeyword.hotkey('Ctrl', 'K')

    @staticmethod
    def change_default_engine(self):
        """Change the Default Search Engine"""
        self.SearchKeyword.hotkey('Ctrl', 'up')

    @staticmethod
    def view_menu(self):
        """View menu to switch, add or manage search engines"""
        self.SearchKeyword.hotkey('Alt', 'down')
        
          
class Navigation():
    """Firefox Browser navigation class"""
    def __init__(self):
        self.navBrowser = pyauto

    @staticmethod
    def back(self):
        """Go back"""
        self.navBrowser.hotkey('Alt', 'left')

    @staticmethod
    def forward(self):
        """Go forward"""
        self.navBrowser.hotkey('Alt', 'right')

    @staticmethod
    def home(self):
        """go to the home web page"""
        self.navBrowser.hotkey('Alt', 'Home')

    @staticmethod
    def open_file(self):
        """Open folder"""
        self.navBrowser.hotkey('Ctrl', 'o')

    @staticmethod
    def reload(self):
        """Reload page """
        self.navBrowser.hotkey('F5') or pygui.hotkey('Ctrl', 'R')

    @staticmethod
    def reload_cache(self):
        """Reload page and cache"""
        self.navBrowser.hotkey('Ctrl', 'F5') or pygui.hotkey('Ctrl', 'Shift', 'R')

    @staticmethod
    def stop(self):
        """Stop the requests"""
        self.navBrowser.hotkey('Esc')
        
        
class Edit():
    """Contains command to edit the text in web page"""
    def __init__(self):
        self.EditKeyboard = pygui

    @staticmethod
    def copy(self):
        """Copy the selected contend"""
        self.EditKeyboard.hotkey('Ctrl', 'C')

    @staticmethod
    def cut(self):
        """Cut the selected content"""
        self.EditKeyboard.hotkey('Ctrl', 'X')

    @staticmethod
    def delete(self):
        """Deletes when the contents is selected"""
        self.EditKeyboard.hotkey('Del')

    @staticmethod
    def delete_left_world(self):
        """Delete the world on the left"""
        self.EditKeyboard.hotkey('Ctrl', 'Backspace')

    @staticmethod
    def delete_right_world(self):
        """Delete the word on the right"""
        self.EditKeyboard.hotkey('Ctrl', 'Del')

    @staticmethod
    def go_one_world_left(self):
        """Move the cursor one word left"""
        self.EditKeyboard.hotkey('Ctrl', '+', 'Left')

    @staticmethod
    def go_one_world_right(self):
        """Move cursor one word right"""
        self.EditKeyboard.hotkey('Ctrl', '+', 'Right')

    @staticmethod
    def go_line_beginning(self):
        """Go to the beginning of the line"""
        self.EditKeyboard.hotkey('Home')

    @staticmethod
    def go_line_end(self):
        """Go to the end of the line"""
        self.EditKeyboard.hotkey('End')

    @staticmethod
    def go_text_beginning(self):
        """Go to the beginning of the text"""
        self.EditKeyboard.hotkey('Ctrl', 'Home')

    @staticmethod
    def go_end_text(self):
        """Go to the end of the text"""
        self.EditKeyboard.hotkey('Ctrl', 'End')

    @staticmethod
    def paste(self):
        """Past what ever is in clipboard"""
        self.EditKeyboard.hotkey('Ctrl', 'V')

    @staticmethod
    def paste_as_plain(self):
        """Paste as plain"""
        self.EditKeyboard.hotkey('Ctrl', 'Shift', 'V')

    @staticmethod
    def redo(self):
        """Redo action"""
        self.EditKeyboard.hotkey('Ctrl', 'Shift', 'Z')

    @staticmethod
    def select_all(self):
        """Select all content"""
        self.EditKeyboard.hotkey('Ctrl', 'A')

    @staticmethod
    def undo(self):
        """Undo action"""
        self.EditKeyboard.hotkey('Ctrl', 'Z')


class Page():
    def __init__(self):
    """Shortcuts working with a web page"""
        self.pageContrl = pyauto

    @staticmethod
    def focus_next(self):
        """Go to next focus"""
        self.pageContrl.hotkey('Tab')

    @staticmethod
    def previous_focus(self):
        """Go to previous focus"""
        self.pageContrl.hotkey('Shift', 'Tab')

    @staticmethod
    def go_down(self):
        """Go down the page"""
        self.pageContrl.hotkey('Down') or pygui.hotkey('Space')

    @staticmethod
    def go_up(self):
        """Go up the page"""
        self.pageContrl.hotkey('Up') or pygui.hotkey('Shift', 'Space')

    @staticmethod
    def go_bottom(self):
        """Go to the bottom of the page"""
        self.pageContrl.hotkey('End')

    @staticmethod
    def go_top(self):
        """Go to the top of page"""
        self.pageContrl.hotkey('Home')

    @staticmethod
    def next_frame(self):
        """Go to next frame"""
        self.pageContrl.hotkey('F6')

    @staticmethod
    def previous_frame(self):
        """Go to previous frame"""
        self.pageContrl.hotkey('Shift', 'F6')

    @staticmethod
    def print_page(self):
        """Print the page"""
        self.pageContrl.hotkey('Ctrl', 'P')

    @staticmethod
    def save_focused_link(self):
        """Save the focused link it works when browser.altClickSave is set to true"""
        self.pageContrl.hotkey('Alt', 'Enter')

    @staticmethod
    def save_page_as(self):
        """Save the page as, yuo chose the name and destination to save it"""
        self.pageContrl.hotkey('Ctrl', 's')

    @staticmethod
    def zoom_in(self):
        """Zoom in the page"""
        self.pageContrl.hotkey('Ctrl', '+')

    @staticmethod
    def zoom_out(self):
        """Zoom out the page"""
        self.pageContrl.hotkey('Ctrl', '-')

    @staticmethod
    def reset_zoom(self):
        """Reset the zoom to 0"""
        self.pageContrl.hotkey('Ctrl', '0')
