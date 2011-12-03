import sublime
import sublime_plugin


class SublimeBlockCursor(sublime_plugin.EventListener):
    def view_is_widget(view):
        settings = view.settings()
        return bool(settings.get('is_widget'))

    def show_block_cursor(self, view, reg):
        view.add_regions('SublimeBlockCursorListener', [sublime.Region(reg.a, reg.a + 1)], 'block_cursor')

    def on_selection_modified(self, view):
        reg = view.sel()[0]
        if view.settings().get('is_widget') or not view.settings().get('command_mode') or reg.a != reg.b:
            view.erase_regions('SublimeBlockCursorListener')
            return
        self.show_block_cursor(view, reg)

    def on_deactivated(self, view):
        view.erase_regions('SublimeBlockCursorListener')

    def on_activated(self, view):
        self.show_block_cursor(view, view.sel()[0])
