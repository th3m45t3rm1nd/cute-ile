#################################
# IMPORTS START
#################################

import os
from libqtile import bar, layout, widget, qtile 
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder

#################################
# IMPORTS END
#################################

mod = "mod4"
terminal = guess_terminal()

#################################
# KEYBINDINGS START
#################################

keys = [
    # Switch between windows
    Key([mod], 
        "h", 
        lazy.layout.left(), 
        desc="Move focus to left"
    ),
    
    Key([mod], 
        "l",
        lazy.layout.right(), 
        desc="Move focus to right"
    ),
    
    Key([mod], 
        "j", 
        lazy.layout.down(), 
        desc="Move focus down"
    ),
    
    Key([mod], 
        "k", 
        lazy.layout.up(), 
        desc="Move focus up"
    ),
    
    Key([mod], 
        "space",
        lazy.layout.next(), 
        desc="Move window focus to other window"
    ),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    
    Key([mod, "shift"], 
        "l", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
    ),
    
    Key([mod, "shift"], 
        "j", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"
    ),
    
    Key([mod, "shift"], 
        "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
    ),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    
    Key([mod, "control"], 
        "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
    ),
    
    Key([mod, "control"], 
        "l", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"
    ),
    
    Key([mod, "control"], 
        "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
    ),
    
    Key([mod, "control"], 
        "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),
    
    Key([mod], 
        "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
    ),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    
    Key([mod], 
        "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),
    
    # Toggle between different layouts as defined below
    Key([mod], 
        "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
    ),
    
    Key([mod], 
        "w",
        lazy.window.kill(), 
        desc="Kill focused window"
    ),
    
    Key([mod, "control"], 
        "r", 
        lazy.reload_config(), 
        desc="Reload the config"
    ),
    
    Key([mod, "control"], 
        "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),
    
    Key([mod], 
        "r", 
        lazy.spawncmd(), 
        desc="Spawn a command using a prompt widget"
    ),
]

#################################
# KEYBINDINGS END
#################################

groups = [Group("一", layout='monadtall'),
          Group("二", layout='monadtall'),
          Group("三", layout='monadtall'),
          Group("四", layout='monadtall'),
          Group("五", layout='monadtall'),
          Group("六", layout='monadtall'),
          Group("七", layout='monadtall'),
          Group("八", layout='monadtall'),
          Group("九", layout='monadtall'),
          Group("十",  layout='floating')
]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder("mod4")

#################################
# LAYOUT START
#################################

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

#################################
# LAYOUT END
#################################

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

#################################
# WIDGET START
#################################
widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize = 14,
    padding = 0,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

#################################
# WIDGET END
#################################

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.Image(
                       filename = "~/.config/qtile/icons/python.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}
                       ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 14,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
                widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
                widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 5
                       ),
                widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
                widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
                widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
                widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
                widget.Net(
                       interface = "wlo1",
                       format = 'Net: {down} ↓↑ {up}',
                       foreground = colors[3],
                       background = colors[0],
                       padding = 5
                       ),
                widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
                widget.CPU(
                       foreground = colors[4],
                       background = colors[0],
                       threshold = 90,
                       format = 'CPU:  {freq_current}GHz {load_percent}%',
                       padding = 5
                       ),
                widget.TextBox(
                       text='|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
                #widget.CheckUpdates(
                #       update_interval = 1800,
                #       distro = "Arch_checkupdates",
                #       display_format = "Updates: {updates} ",
                #       foreground = colors[1],
                #       colour_have_updates = colors[1],
                #       colour_no_updates = colors[1],
                #       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                #       padding = 5,
                #       background = colors[5]
                #       ),
                #widget.TextBox(
                #        text = '',
                #        font = "Ubuntu Mono",
                #        background = colors[5],
                #       foreground = colors[6],
                #        padding = 0,
                #       fontsize = 37
                #        ),
                widget.Memory(
                       foreground = colors[6],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                       fmt = 'Mem: {}',
                       padding = 5
                       ),
                widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
                widget.Volume(
                       foreground = colors[7],
                       background = colors[0],
                       fmt = 'Vol: {}',
                       padding = 5
                       ),
               #widget.TextBox(
               #         text = '',
               #         font = "Ubuntu Mono",
               #         background = colors[7],
               #         foreground = colors[8],
               #         padding = 0,
               #         fontsize = 37
               #         ),
               #widget.KeyboardLayout(
               #         foreground = colors[1],
               #         background = colors[8],
               #         fmt = 'Keyboard: {}',
               #         padding = 5
               #         ),
                widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
                widget.Clock(
                       foreground = colors[9],
                       background = colors[0],
                       format = "%A, %B %d - %H:%M "
                       ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
