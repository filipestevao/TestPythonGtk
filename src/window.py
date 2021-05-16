# window.py
#
# Copyright 2021 filipestevao
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


@Gtk.Template(resource_path='/io/github/filipestevao/TestPythonGtk/window.ui')
class TestpythongtkWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'TestpythongtkWindow'

    entry1 = Gtk.Template.Child()
    button1 = Gtk.Template.Child()
    label1 = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Connect children with their functions
        self.entry1.connect("changed", self.textEntry)
        self.button1.connect("clicked", self.onClicked)

    def textEntry(self, *args, **kargs):
        self.entryText = self.entry1.get_text()

    def onClicked(self, *args, **kargs):
        try:
            self.label1.set_text(f"Hello {self.entryText}!")
        except AttributeError:
            pass
