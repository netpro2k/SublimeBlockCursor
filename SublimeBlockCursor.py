import sublime
import sublime_plugin


class SublimeBlockCursor(sublime_plugin.EventListener):
    def view_is_widget(view):
        settings = view.settings()
        return bool(settings.get('is_widget'))

    def show_block_cursor(self, view):
        validRegions = []
        for s in view.sel():
            if s.a != s.b:
                continue
            validRegions.append(sublime.Region(s.a, s.a + 1))
        if validRegions.__len__:
            view.add_regions('SublimeBlockCursorListener', validRegions, 'block_cursor')
        else:
            view.erase_regions('SublimeBlockCursorListener')

    def on_selection_modified(self, view):
        if view.settings().get('is_widget') or not view.settings().get('command_mode'):
            view.erase_regions('SublimeBlockCursorListener')
            return
        self.show_block_cursor(view)

    def on_deactivated(self, view):
        view.erase_regions('SublimeBlockCursorListener')
        view.settings().clear_on_change('command_mode')
        self.current_view = None

    def on_activated(self, view):
        self.on_selection_modified(view)
        view.settings().add_on_change('command_mode', self.on_command_mode_change)
        self.current_view = view

    def on_command_mode_change(self):
        self.on_selection_modified(self.current_view)