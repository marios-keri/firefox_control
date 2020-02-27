"""Control Firefox through shortcuts"""

import pyautogui as auto


class Search:
    """Search commands for firefox"""
    def __init__(self):
        self.search_keyword = auto

    def find(self):
        """find in the document"""
        self.search_keyword.hotkey('Ctrl', 'F')

    def find_again(self):
        """Find Again"""
        self.search_keyword.hotkey('F3')

    def find_previous(self):
        """Find Previous"""
        self.search_keyword.hotkey('Shift', 'F3')

    def quick_find_within_link_text(self):
        """Quick Find within link-text only"""
        self.search_keyword.hotkey("'")

    def quick_find(self):
        """Quick Find"""
        self.search_keyword.hotkey('/')

    def close_find(self):
        """Close the Find or Quick Find bar"""
        self.search_keyword.hotkey('Esc')

    def focus_search_bar(self):
        """Focus Search bar"""
        self.search_keyword.hotkey('Ctrl', 'K')

    def change_default_engine(self):
        """Change the Default Search Engine"""
        self.search_keyword.hotkey('Ctrl', 'up')

    def view_menu(self):
        """View menu to switch, add or manage search engines"""
        self.search_keyword.hotkey('Alt', 'down')
        
          
class Navigation:
    """Firefox Browser navigation class"""
    def __init__(self):
        self.nav_browser = auto

    def back(self):
        """Go back"""
        self.nav_browser.hotkey('Alt', 'left')

    def forward(self):
        """Go forward"""
        self.nav_browser.hotkey('Alt', 'right')

    def home(self):
        """go to the home web page"""
        self.nav_browser.hotkey('Alt', 'Home')

    def open_file(self):
        """Open folder"""
        self.nav_browser.hotkey('Ctrl', 'o')

    def reload(self):
        """Reload page """
        self.nav_browser.hotkey('F5')

    def reload_cache(self):
        """Reload page and cache"""
        self.nav_browser.hotkey('Ctrl', 'F5')

    def stop(self):
        """Stop the requests"""
        self.nav_browser.hotkey('Esc')
        
        
class Edit:
    """Contains command to edit the text in web page"""
    def __init__(self):
        self.edit_keyboard = auto

    def copy(self):
        """Copy the selected contend"""
        self.edit_keyboard.hotkey('Ctrl', 'C')

    def cut(self):
        """Cut the selected content"""
        self.edit_keyboard.hotkey('Ctrl', 'X')

    def delete(self):
        """Deletes when the contents is selected"""
        self.edit_keyboard.hotkey('Del')

    def delete_left_world(self):
        """Delete the world on the left"""
        self.edit_keyboard.hotkey('Ctrl', 'Backspace')

    def delete_right_world(self):
        """Delete the word on the right"""
        self.edit_keyboard.hotkey('Ctrl', 'Del')

    def go_one_world_left(self):
        """Move the cursor one word left"""
        self.edit_keyboard.hotkey('Ctrl', '+', 'Left')

    def go_one_world_right(self):
        """Move cursor one word right"""
        self.edit_keyboard.hotkey('Ctrl', '+', 'Right')

    def go_line_beginning(self):
        """Go to the beginning of the line"""
        self.edit_keyboard.hotkey('Home')

    def go_line_end(self):
        """Go to the end of the line"""
        self.edit_keyboard.hotkey('End')

    def go_text_beginning(self):
        """Go to the beginning of the text"""
        self.edit_keyboard.hotkey('Ctrl', 'Home')

    def go_end_text(self):
        """Go to the end of the text"""
        self.edit_keyboard.hotkey('Ctrl', 'End')

    def paste(self):
        """Past what ever is in clipboard"""
        self.edit_keyboard.hotkey('Ctrl', 'V')

    def paste_as_plain(self):
        """Paste as plain"""
        self.edit_keyboard.hotkey('Ctrl', 'Shift', 'V')

    def redo(self):
        """Redo action"""
        self.edit_keyboard.hotkey('Ctrl', 'Shift', 'Z')

    def select_all(self):
        """Select all content"""
        self.edit_keyboard.hotkey('Ctrl', 'A')

    def undo(self):
        """Undo action"""
        self.edit_keyboard.hotkey('Ctrl', 'Z')


class Page:
    """working os the content of the page"""

    def __init__(self):
        """Shortcuts working with a web page"""
        self.page_control = auto

    def focus_next(self):
        """Go to next focus"""
        self.page_control.hotkey('Tab')

    def previous_focus(self):
        """Go to previous focus"""
        self.page_control.hotkey('Shift', 'Tab')

    def go_down(self):
        """Go down the page"""
        self.page_control.hotkey('Down')

    def go_up(self):
        """Go up the page"""
        self.page_control.hotkey('Up')

    def go_bottom(self):
        """Go to the bottom of the page"""
        self.page_control.hotkey('End')

    def go_top(self):
        """Go to the top of page"""
        self.page_control.hotkey('Home')

    def next_frame(self):
        """Go to next frame"""
        self.page_control.hotkey('F6')

    def previous_frame(self):
        """Go to previous frame"""
        self.page_control.hotkey('Shift', 'F6')

    def print_page(self):
        """Print the page"""
        self.page_control.hotkey('Ctrl', 'P')

    def save_focused_link(self):
        """Save the focused link it works when browser.altClickSave is set to true"""
        self.page_control.hotkey('Alt', 'Enter')

    def save_page_as(self):
        """Save the page as, yuo chose the name and destination to save it"""
        self.page_control.hotkey('Ctrl', 's')

    def zoom_in(self):
        """Zoom in the page"""
        self.page_control.hotkey('Ctrl', '+')

    def zoom_out(self):
        """Zoom out the page"""
        self.page_control.hotkey('Ctrl', '-')

    def reset_zoom(self):
        """Reset the zoom to 0"""
        self.page_control.hotkey('Ctrl', '0')

        
class Tools:
    """Working with the borwser's tool box"""
    def __init__(self):
        self.tool_box = auto

    def downloads(self):
        """open downloads"""
        self.tool_box.hotkey('Ctrl', 'Shift', 'Y')

    def add_ons(self):
        """open add ons"""
        self.tool_box.hotkey('Ctrl', 'Shift', 'A')

    def developer_tools(self):
        """open tool box"""
        self.tool_box.hotkey('F12')

    def web_console(self):
        """open web console"""
        self.tool_box.hotkey('Ctrl', 'Shift', 'K')

    def inspector(self):
        """open inspector"""
        self.tool_box.hotkey('Ctrl', 'Shift', 'C')

    def debugger(self):
        """open debugger"""
        self.tool_box.hotkey('Ctrl', 'Shift', 'S')

    def style_editor(self):
        """open style editor tool box"""
        self.tool_box.hotkey('Shift', 'F7')

    def profiler(self):
        """open profiler tool box"""
        self.tool_box.hotkey('Shift', 'F5')

    def network(self):
        """open network tool box"""
        self.tool_box.hotkey('Ctrl', 'Shift', 'E')

    def developer(self):
        """open developer tool box"""
        self.tool_box.hotkey('Shift', 'F2')

    def design_view(self):
        """open design view"""
        self.tool_box.hotkey('Ctrl', 'Shift', 'M')

    def scratchpad(self):
        """open scratch pad"""
        self.tool_box.hotkey('Shift', 'F4')

    def page_source(self):
        """open the source code in new tab"""
        self.tool_box.hotkey('Ctrl', 'u')

    def console(self):
        """"open browser console"""
        self.tool_box.hotkey('Ctrl', 'Shift', 'j')

    def page_info(self):
        """view page info"""
        self.tool_box.hotkey('Ctrl', 'I')

# one test case
if __name__ == '__main__':
    firefox = Tools()
    import time
    time.sleep(8)
    firefox.console()
