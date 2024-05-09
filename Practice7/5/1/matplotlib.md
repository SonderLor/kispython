# Модуль matplotlib

An object-oriented plotting library.

A procedural interface is provided by the companion pyplot module,
which may be imported directly, e.g.::

    import matplotlib.pyplot as plt

or using ipython::

    ipython

at your terminal, followed by::

    In [1]: %matplotlib
    In [2]: import matplotlib.pyplot as plt

at the ipython shell prompt.

For the most part, direct use of the explicit object-oriented library is
encouraged when programming; the implicit pyplot interface is primarily for
working interactively. The exceptions to this suggestion are the pyplot
functions `.pyplot.figure`, `.pyplot.subplot`, `.pyplot.subplots`, and
`.pyplot.savefig`, which can greatly simplify scripting.  See
:ref:`api_interfaces` for an explanation of the tradeoffs between the implicit
and explicit interfaces.

Modules include:

:mod:`matplotlib.axes`
    The `~.axes.Axes` class.  Most pyplot functions are wrappers for
    `~.axes.Axes` methods.  The axes module is the highest level of OO
    access to the library.

:mod:`matplotlib.figure`
    The `.Figure` class.

:mod:`matplotlib.artist`
    The `.Artist` base class for all classes that draw things.

:mod:`matplotlib.lines`
    The `.Line2D` class for drawing lines and markers.

:mod:`matplotlib.patches`
    Classes for drawing polygons.

:mod:`matplotlib.text`
    The `.Text` and `.Annotation` classes.

:mod:`matplotlib.image`
    The `.AxesImage` and `.FigureImage` classes.

:mod:`matplotlib.collections`
    Classes for efficient drawing of groups of lines or polygons.

:mod:`matplotlib.colors`
    Color specifications and making colormaps.

:mod:`matplotlib.cm`
    Colormaps, and the `.ScalarMappable` mixin class for providing color
    mapping functionality to other classes.

:mod:`matplotlib.ticker`
    Calculation of tick mark locations and formatting of tick labels.

:mod:`matplotlib.backends`
    A subpackage with modules for various GUI libraries and output formats.

The base matplotlib namespace includes:

`~matplotlib.rcParams`
    Default configuration settings; their defaults may be overridden using
    a :file:`matplotlibrc` file.

`~matplotlib.use`
    Setting the Matplotlib backend.  This should be called before any
    figure is created, because it is not possible to switch between
    different GUI backends after that.

The following environment variables can be used to customize the behavior:

:envvar:`MPLBACKEND`
    This optional variable can be set to choose the Matplotlib backend. See
    :ref:`what-is-a-backend`.

:envvar:`MPLCONFIGDIR`
    This is the directory used to store user customizations to
    Matplotlib, as well as some caches to improve performance. If
    :envvar:`MPLCONFIGDIR` is not defined, :file:`{HOME}/.config/matplotlib`
    and :file:`{HOME}/.cache/matplotlib` are used on Linux, and
    :file:`{HOME}/.matplotlib` on other platforms, if they are
    writable. Otherwise, the Python standard library's `tempfile.gettempdir`
    is used to find a base directory in which the :file:`matplotlib`
    subdirectory is created.

Matplotlib was initially written by John D. Hunter (1968-2012) and is now
developed and maintained by a host of others.

Occasionally the internal documentation (python docstrings) will refer
to MATLAB®, a registered trademark of The MathWorks, Inc.

## Класс ExecutableNotFoundError
Error raised when an executable that Matplotlib optionally
    depends on can't be found.
## Класс MatplotlibDeprecationWarning
A class for issuing deprecation warnings for Matplotlib users.
## Класс MutableMapping
A MutableMapping is a generic container for associating
    key/value pairs.

    This class provides concrete generic implementations of all
    methods except for __getitem__, __setitem__, __delitem__,
    __iter__, and __len__.
## Класс Parameter
Represents a parameter in a function signature.

    Has the following public attributes:

    * name : str
        The name of the parameter as a string.
    * default : object
        The default value for the parameter if specified.  If the
        parameter has no default value, this attribute is set to
        `Parameter.empty`.
    * annotation
        The annotation for the parameter if specified.  If the
        parameter has no annotation, this attribute is set to
        `Parameter.empty`.
    * kind : str
        Describes how argument values are bound to the parameter.
        Possible values: `Parameter.POSITIONAL_ONLY`,
        `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`,
        `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.
* **Метод** `replace(self, *, name=_void, kind=_void`
Creates a customized copy of the Parameter.
## Класс Path
PurePath subclass that can make system calls.

    Path represents a filesystem path but unlike PurePath, also offers
    methods to do system calls on path objects. Depending on your system,
    instantiating a Path will return either a PosixPath or a WindowsPath
    object. You can also instantiate a PosixPath or WindowsPath directly,
    but cannot instantiate a WindowsPath on a POSIX system or vice versa.
* **Метод** `__bytes__(self)`
Return the bytes representation of the path.  This is only
        recommended to use under Unix.
* **Метод** `__str__(self)`
Return the string representation of the path, suitable for
        passing to system calls.
* **Метод** `absolute(self)`
Return an absolute version of this path by prepending the current
        working directory. No normalization or symlink resolution is performed.

        Use resolve() to get the canonical path to a file.
* **Метод** `as_posix(self)`
Return the string representation of the path with forward (/)
        slashes.
* **Метод** `as_uri(self)`
Return the path as a 'file' URI.
* **Метод** `chmod(self, mode, *, follow_symlinks=True)`
Change the permissions of the path, like os.chmod().
* **Метод** `exists(self)`
Whether this path exists.
* **Метод** `expanduser(self)`
Return a new path with expanded ~ and ~user constructs
        (as returned by os.path.expanduser)
* **Метод** `glob(self, pattern)`
Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
* **Метод** `group(self)`
Return the group name of the file gid.
* **Метод** `hardlink_to(self, target)`
Make this path a hard link pointing to the same file as *target*.

        Note the order of arguments (self, target) is the reverse of os.link's.
* **Метод** `is_absolute(self)`
True if the path is absolute (has both a root and, if applicable,
        a drive).
* **Метод** `is_block_device(self)`
Whether this path is a block device.
* **Метод** `is_char_device(self)`
Whether this path is a character device.
* **Метод** `is_dir(self)`
Whether this path is a directory.
* **Метод** `is_fifo(self)`
Whether this path is a FIFO.
* **Метод** `is_file(self)`
Whether this path is a regular file (also True for symlinks pointing
        to regular files).
* **Метод** `is_mount(self)`
Check if this path is a POSIX mount point
* **Метод** `is_relative_to(self, *other)`
Return True if the path is relative to another path or False.
* **Метод** `is_reserved(self)`
Return True if the path contains one of the special names reserved
        by the system, if any.
* **Метод** `is_socket(self)`
Whether this path is a socket.
* **Метод** `is_symlink(self)`
Whether this path is a symbolic link.
* **Метод** `iterdir(self)`
Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
* **Метод** `joinpath(self, *args)`
Combine this path with one or several arguments, and return a
        new path representing either a subpath (if all arguments are relative
        paths) or a totally different path (if one of the arguments is
        anchored).
* **Метод** `lchmod(self, mode)`
Like chmod(), except if the path points to a symlink, the symlink's
        permissions are changed, rather than its target's.
* **Метод** `link_to(self, target)`
Make the target path a hard link pointing to this path.

        Note this function does not make this path a hard link to *target*,
        despite the implication of the function and argument names. The order
        of arguments (target, link) is the reverse of Path.symlink_to, but
        matches that of os.link.

        Deprecated since Python 3.10 and scheduled for removal in Python 3.12.
        Use `hardlink_to()` instead.
* **Метод** `lstat(self)`
Like stat(), except if the path points to a symlink, the symlink's
        status information is returned, rather than its target's.
* **Метод** `match(self, path_pattern)`
Return True if this path matches the given pattern.
* **Метод** `mkdir(self, mode=0o777, parents=False, exist_ok=False)`
Create a new directory at this given path.
* **Метод** `open(self, mode='r', buffering=-1, encoding=None`
Open the file pointed by this path and return a file object, as
        the built-in open() function does.
* **Метод** `owner(self)`
Return the login name of the file owner.
* **Метод** `read_bytes(self)`
Open the file in bytes mode, read it, and close the file.
* **Метод** `read_text(self, encoding=None, errors=None)`
Open the file in text mode, read it, and close the file.
* **Метод** `readlink(self)`
Return the path to which the symbolic link points.
* **Метод** `relative_to(self, *other)`
Return the relative path to another path identified by the passed
        arguments.  If the operation is not possible (because this is not
        a subpath of the other path), raise ValueError.
* **Метод** `rename(self, target)`
Rename this path to the target path.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
* **Метод** `replace(self, target)`
Rename this path to the target path, overwriting if that path exists.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
* **Метод** `resolve(self, strict=False)`
Make the path absolute, resolving all symlinks on the way and also
        normalizing it.
* **Метод** `rglob(self, pattern)`
Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
* **Метод** `rmdir(self)`
Remove this directory.  The directory must be empty.
* **Метод** `samefile(self, other_path)`
Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
* **Метод** `stat(self, *, follow_symlinks=True)`
Return the result of the stat() system call on this path, like
        os.stat() does.
* **Метод** `symlink_to(self, target, target_is_directory=False)`
Make this path a symlink pointing to the target path.
        Note the order of arguments (link, target) is the reverse of os.symlink.
* **Метод** `touch(self, mode=0o666, exist_ok=True)`
Create this file with the given access mode, if it doesn't exist.
* **Метод** `unlink(self, missing_ok=False)`
Remove this file or link.
        If the path is a directory, use rmdir() instead.
* **Метод** `with_name(self, name)`
Return a new path with the file name changed.
* **Метод** `with_stem(self, stem)`
Return a new path with the stem changed.
* **Метод** `with_suffix(self, suffix)`
Return a new path with the file suffix changed.  If the path
        has no suffix, add given suffix.  If the given suffix is an empty
        string, remove the suffix from the path.
* **Метод** `write_bytes(self, data)`
Open the file in bytes mode, write to it, and close the file.
* **Метод** `write_text(self, data, encoding=None, errors=None, newline=None)`
Open the file in text mode, write to it, and close the file.
## Класс RcParams
A dict-like key-value store for config parameters, including validation.

Validating functions are defined and associated with rc parameters in
:mod:`matplotlib.rcsetup`.

The list of rcParams is:

- _internal.classic_mode
- agg.path.chunksize
- animation.bitrate
- animation.codec
- animation.convert_args
- animation.convert_path
- animation.embed_limit
- animation.ffmpeg_args
- animation.ffmpeg_path
- animation.frame_format
- animation.html
- animation.writer
- axes.autolimit_mode
- axes.axisbelow
- axes.edgecolor
- axes.facecolor
- axes.formatter.limits
- axes.formatter.min_exponent
- axes.formatter.offset_threshold
- axes.formatter.use_locale
- axes.formatter.use_mathtext
- axes.formatter.useoffset
- axes.grid
- axes.grid.axis
- axes.grid.which
- axes.labelcolor
- axes.labelpad
- axes.labelsize
- axes.labelweight
- axes.linewidth
- axes.prop_cycle
- axes.spines.bottom
- axes.spines.left
- axes.spines.right
- axes.spines.top
- axes.titlecolor
- axes.titlelocation
- axes.titlepad
- axes.titlesize
- axes.titleweight
- axes.titley
- axes.unicode_minus
- axes.xmargin
- axes.ymargin
- axes.zmargin
- axes3d.grid
- axes3d.xaxis.panecolor
- axes3d.yaxis.panecolor
- axes3d.zaxis.panecolor
- backend
- backend_fallback
- boxplot.bootstrap
- boxplot.boxprops.color
- boxplot.boxprops.linestyle
- boxplot.boxprops.linewidth
- boxplot.capprops.color
- boxplot.capprops.linestyle
- boxplot.capprops.linewidth
- boxplot.flierprops.color
- boxplot.flierprops.linestyle
- boxplot.flierprops.linewidth
- boxplot.flierprops.marker
- boxplot.flierprops.markeredgecolor
- boxplot.flierprops.markeredgewidth
- boxplot.flierprops.markerfacecolor
- boxplot.flierprops.markersize
- boxplot.meanline
- boxplot.meanprops.color
- boxplot.meanprops.linestyle
- boxplot.meanprops.linewidth
- boxplot.meanprops.marker
- boxplot.meanprops.markeredgecolor
- boxplot.meanprops.markerfacecolor
- boxplot.meanprops.markersize
- boxplot.medianprops.color
- boxplot.medianprops.linestyle
- boxplot.medianprops.linewidth
- boxplot.notch
- boxplot.patchartist
- boxplot.showbox
- boxplot.showcaps
- boxplot.showfliers
- boxplot.showmeans
- boxplot.vertical
- boxplot.whiskerprops.color
- boxplot.whiskerprops.linestyle
- boxplot.whiskerprops.linewidth
- boxplot.whiskers
- contour.algorithm
- contour.corner_mask
- contour.linewidth
- contour.negative_linestyle
- date.autoformatter.day
- date.autoformatter.hour
- date.autoformatter.microsecond
- date.autoformatter.minute
- date.autoformatter.month
- date.autoformatter.second
- date.autoformatter.year
- date.converter
- date.epoch
- date.interval_multiples
- docstring.hardcopy
- errorbar.capsize
- figure.autolayout
- figure.constrained_layout.h_pad
- figure.constrained_layout.hspace
- figure.constrained_layout.use
- figure.constrained_layout.w_pad
- figure.constrained_layout.wspace
- figure.dpi
- figure.edgecolor
- figure.facecolor
- figure.figsize
- figure.frameon
- figure.hooks
- figure.labelsize
- figure.labelweight
- figure.max_open_warning
- figure.raise_window
- figure.subplot.bottom
- figure.subplot.hspace
- figure.subplot.left
- figure.subplot.right
- figure.subplot.top
- figure.subplot.wspace
- figure.titlesize
- figure.titleweight
- font.cursive
- font.family
- font.fantasy
- font.monospace
- font.sans-serif
- font.serif
- font.size
- font.stretch
- font.style
- font.variant
- font.weight
- grid.alpha
- grid.color
- grid.linestyle
- grid.linewidth
- hatch.color
- hatch.linewidth
- hist.bins
- image.aspect
- image.cmap
- image.composite_image
- image.interpolation
- image.lut
- image.origin
- image.resample
- interactive
- keymap.back
- keymap.copy
- keymap.forward
- keymap.fullscreen
- keymap.grid
- keymap.grid_minor
- keymap.help
- keymap.home
- keymap.pan
- keymap.quit
- keymap.quit_all
- keymap.save
- keymap.xscale
- keymap.yscale
- keymap.zoom
- legend.borderaxespad
- legend.borderpad
- legend.columnspacing
- legend.edgecolor
- legend.facecolor
- legend.fancybox
- legend.fontsize
- legend.framealpha
- legend.frameon
- legend.handleheight
- legend.handlelength
- legend.handletextpad
- legend.labelcolor
- legend.labelspacing
- legend.loc
- legend.markerscale
- legend.numpoints
- legend.scatterpoints
- legend.shadow
- legend.title_fontsize
- lines.antialiased
- lines.color
- lines.dash_capstyle
- lines.dash_joinstyle
- lines.dashdot_pattern
- lines.dashed_pattern
- lines.dotted_pattern
- lines.linestyle
- lines.linewidth
- lines.marker
- lines.markeredgecolor
- lines.markeredgewidth
- lines.markerfacecolor
- lines.markersize
- lines.scale_dashes
- lines.solid_capstyle
- lines.solid_joinstyle
- macosx.window_mode
- markers.fillstyle
- mathtext.bf
- mathtext.bfit
- mathtext.cal
- mathtext.default
- mathtext.fallback
- mathtext.fontset
- mathtext.it
- mathtext.rm
- mathtext.sf
- mathtext.tt
- patch.antialiased
- patch.edgecolor
- patch.facecolor
- patch.force_edgecolor
- patch.linewidth
- path.effects
- path.simplify
- path.simplify_threshold
- path.sketch
- path.snap
- pcolor.shading
- pcolormesh.snap
- pdf.compression
- pdf.fonttype
- pdf.inheritcolor
- pdf.use14corefonts
- pgf.preamble
- pgf.rcfonts
- pgf.texsystem
- polaraxes.grid
- ps.distiller.res
- ps.fonttype
- ps.papersize
- ps.useafm
- ps.usedistiller
- savefig.bbox
- savefig.directory
- savefig.dpi
- savefig.edgecolor
- savefig.facecolor
- savefig.format
- savefig.orientation
- savefig.pad_inches
- savefig.transparent
- scatter.edgecolors
- scatter.marker
- svg.fonttype
- svg.hashsalt
- svg.image_inline
- text.antialiased
- text.color
- text.hinting
- text.hinting_factor
- text.kerning_factor
- text.latex.preamble
- text.parse_math
- text.usetex
- timezone
- tk.window_focus
- toolbar
- webagg.address
- webagg.open_in_browser
- webagg.port
- webagg.port_retries
- xaxis.labellocation
- xtick.alignment
- xtick.bottom
- xtick.color
- xtick.direction
- xtick.labelbottom
- xtick.labelcolor
- xtick.labelsize
- xtick.labeltop
- xtick.major.bottom
- xtick.major.pad
- xtick.major.size
- xtick.major.top
- xtick.major.width
- xtick.minor.bottom
- xtick.minor.ndivs
- xtick.minor.pad
- xtick.minor.size
- xtick.minor.top
- xtick.minor.visible
- xtick.minor.width
- xtick.top
- yaxis.labellocation
- ytick.alignment
- ytick.color
- ytick.direction
- ytick.labelcolor
- ytick.labelleft
- ytick.labelright
- ytick.labelsize
- ytick.left
- ytick.major.left
- ytick.major.pad
- ytick.major.right
- ytick.major.size
- ytick.major.width
- ytick.minor.left
- ytick.minor.ndivs
- ytick.minor.pad
- ytick.minor.right
- ytick.minor.size
- ytick.minor.visible
- ytick.minor.width
- ytick.right

See Also
--------
:ref:`customizing-with-matplotlibrc-files`
* **Метод** `__iter__(self)`
Yield sorted list of keys.
* **Метод** `_get(self, key)`
Directly read data bypassing deprecation, backend and validation
        logic.

        Notes
        -----
        As end user or downstream library you almost always should use
        ``val = rcParams[key]`` and not ``_get()``.

        There are only very few special cases that need direct data access.
        These cases previously used ``dict.__getitem__(rcParams, key, val)``,
        which is now deprecated and replaced by ``rcParams._get(key)``.

        Even though private, we guarantee API stability for ``rcParams._get``,
        i.e. it is subject to Matplotlib's API and deprecation policy.

        :meta public:
* **Метод** `_get_backend_or_none(self)`
Get the requested backend, if any, without triggering resolution.
* **Метод** `_set(self, key, val)`
Directly write data bypassing deprecation and validation logic.

        Notes
        -----
        As end user or downstream library you almost always should use
        ``rcParams[key] = val`` and not ``_set()``.

        There are only very few special cases that need direct data access.
        These cases previously used ``dict.__setitem__(rcParams, key, val)``,
        which is now deprecated and replaced by ``rcParams._set(key, val)``.

        Even though private, we guarantee API stability for ``rcParams._set``,
        i.e. it is subject to Matplotlib's API and deprecation policy.

        :meta public:
* **Метод** `copy(self)`
Copy this RcParams instance.
* **Метод** `find_all(self, pattern)`
Return the subset of this RcParams dictionary whose keys match,
        using :func:`re.search`, the given ``pattern``.

        .. note::

            Changes to the returned dictionary are *not* propagated to
            the parent RcParams dictionary.
## Класс _ExecInfo
_ExecInfo(executable, raw_version, version)
* **Метод** `__getnewargs__(self)`
Return self as a plain tuple.  Used by copy and pickle.
* **Метод** `__repr__(self)`
Return a nicely formatted representation string
* **Метод** `_asdict(self)`
Return a new dict which maps field names to their values.
* **Метод** `_replace(self, /, **kwds)`
Return a new _ExecInfo object replacing specified fields with new values
## Класс _VersionInfo
_VersionInfo(major, minor, micro, releaselevel, serial)
* **Метод** `__getnewargs__(self)`
Return self as a plain tuple.  Used by copy and pickle.
* **Метод** `__repr__(self)`
Return a nicely formatted representation string
* **Метод** `_asdict(self)`
Return a new dict which maps field names to their values.
* **Метод** `_replace(self, /, **kwds)`
Return a new _VersionInfo object replacing specified fields with new values
## Функция _add_data_doc
Сигнатура: `_add_data_doc(docstring, replace_names)`
Add documentation for a *data* field to the given docstring.

    Parameters
    ----------
    docstring : str
        The input docstring.
    replace_names : list of str or None
        The list of parameter names which arguments should be replaced by
        ``data[name]`` (if ``data[name]`` does not throw an exception).  If
        None, replacement is attempted for all arguments.

    Returns
    -------
    str
        The augmented docstring.## Функция _get_version
Сигнатура: `_get_version()`
Return the version string used for __version__.## Функция _get_xdg_cache_dir
Сигнатура: `_get_xdg_cache_dir()`
Return the XDG cache directory, according to the XDG base directory spec:

    https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html## Функция _get_xdg_config_dir
Сигнатура: `_get_xdg_config_dir()`
Return the XDG configuration directory, according to the XDG base
    directory spec:

    https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html## Функция _logged_cached
Сигнатура: `_logged_cached(fmt, func=None)`
Decorator that logs a function's return value, and memoizes that value.

    After ::

        @_logged_cached(fmt)
        def func(): ...

    the first call to *func* will log its return value at the DEBUG level using
    %-format string *fmt*, and memoize it; later calls to *func* will directly
    return that value.## Функция _parse_to_version_info
Сигнатура: `_parse_to_version_info(version_str)`
Parse a version string to a namedtuple analogous to sys.version_info.

    See:
    https://packaging.pypa.io/en/latest/version.html#packaging.version.parse
    https://docs.python.org/3/library/sys.html#sys.version_info## Функция _preprocess_data
Сигнатура: `_preprocess_data(func=None, *, replace_names=None, label_namer=None)`
A decorator to add a 'data' kwarg to a function.

    When applied::

        @_preprocess_data()
        def func(ax, *args, **kwargs): ...

    the signature is modified to ``decorated(ax, *args, data=None, **kwargs)``
    with the following behavior:

    - if called with ``data=None``, forward the other arguments to ``func``;
    - otherwise, *data* must be a mapping; for any argument passed in as a
      string ``name``, replace the argument by ``data[name]`` (if this does not
      throw an exception), then forward the arguments to ``func``.

    In either case, any argument that is a `MappingView` is also converted to a
    list.

    Parameters
    ----------
    replace_names : list of str or None, default: None
        The list of parameter names for which lookup into *data* should be
        attempted. If None, replacement is attempted for all arguments.
    label_namer : str, default: None
        If set e.g. to "namer" (which must be a kwarg in the function's
        signature -- not as ``**kwargs``), if the *namer* argument passed in is
        a (string) key of *data* and no *label* kwarg is passed, then use the
        (string) value of the *namer* as *label*. ::

            @_preprocess_data(label_namer="foo")
            def func(foo, label=None): ...

            func("key", data={"key": value})
            # is equivalent to
            func.__wrapped__(value, label="key")## Функция _rc_params_in_file
Сигнатура: `_rc_params_in_file(fname, transform=lambda x: x, fail_on_error=False)`
Construct a `RcParams` instance from file *fname*.

    Unlike `rc_params_from_file`, the configuration class only contains the
    parameters specified in the file (i.e. default values are not filled in).

    Parameters
    ----------
    fname : path-like
        The loaded file.
    transform : callable, default: the identity function
        A function called on each individual line of the file to transform it,
        before further parsing.
    fail_on_error : bool, default: False
        Whether invalid entries should result in an exception or a warning.## Функция _replacer
Сигнатура: `_replacer(data, value)`
Either returns ``data[value]`` or passes ``data`` back, converts either to
    a sequence.## Функция _val_or_rc
Сигнатура: `_val_or_rc(val, rc_name)`
If *val* is None, return ``mpl.rcParams[rc_name]``, otherwise return val.## Функция cycler
Сигнатура: `cycler(*args, **kwargs)`
Create a `~cycler.Cycler` object much like :func:`cycler.cycler`,
    but includes input validation.

    Call signatures::

      cycler(cycler)
      cycler(label=values[, label2=values2[, ...]])
      cycler(label, values)

    Form 1 copies a given `~cycler.Cycler` object.

    Form 2 creates a `~cycler.Cycler` which cycles over one or more
    properties simultaneously. If multiple properties are given, their
    value lists must have the same length.

    Form 3 creates a `~cycler.Cycler` for a single property. This form
    exists for compatibility with the original cycler. Its use is
    discouraged in favor of the kwarg form, i.e. ``cycler(label=values)``.

    Parameters
    ----------
    cycler : Cycler
        Copy constructor for Cycler.

    label : str
        The property key. Must be a valid `.Artist` property.
        For example, 'color' or 'linestyle'. Aliases are allowed,
        such as 'c' for 'color' and 'lw' for 'linewidth'.

    values : iterable
        Finite-length iterable of the property values. These values
        are validated and will raise a ValueError if invalid.

    Returns
    -------
    Cycler
        A new :class:`~cycler.Cycler` for the given properties.

    Examples
    --------
    Creating a cycler for a single property:

    >>> c = cycler(color=['red', 'green', 'blue'])

    Creating a cycler for simultaneously cycling over multiple properties
    (e.g. red circle, green plus, blue cross):

    >>> c = cycler(color=['red', 'green', 'blue'],
    ...            marker=['o', '+', 'x'])## Функция get_backend
Сигнатура: `get_backend()`
Return the name of the current backend.

    See Also
    --------
    matplotlib.use## Функция get_cachedir
Сигнатура: `gged_cached('CACHEDIR=%s'`
Return the string path of the cache directory.

    The procedure used to find the directory is the same as for
    `get_configdir`, except using ``$XDG_CACHE_HOME``/``$HOME/.cache`` instead.## Функция get_configdir
Сигнатура: `gged_cached('CONFIGDIR=%s'`
Return the string path of the configuration directory.

    The directory is chosen as follows:

    1. If the MPLCONFIGDIR environment variable is supplied, choose that.
    2. On Linux, follow the XDG specification and look first in
       ``$XDG_CONFIG_HOME``, if defined, or ``$HOME/.config``.  On other
       platforms, choose ``$HOME/.matplotlib``.
    3. If the chosen directory exists and is writable, use that as the
       configuration directory.
    4. Else, create a temporary directory, and use it as the configuration
       directory.## Функция get_data_path
Сигнатура: `gged_cached('matplotlib data path: %s'`
Return the path to Matplotlib data.## Функция interactive
Сигнатура: `interactive(b)`
Set whether to redraw after every plotting command (e.g. `.pyplot.xlabel`).## Функция is_interactive
Сигнатура: `is_interactive()`
Return whether to redraw after every plotting command.

    .. note::

        This function is only intended for use in backends. End users should
        use `.pyplot.isinteractive` instead.## Функция matplotlib_fname
Сигнатура: `matplotlib_fname()`
Get the location of the config file.

    The file location is determined in the following order

    - ``$PWD/matplotlibrc``
    - ``$MATPLOTLIBRC`` if it is not a directory
    - ``$MATPLOTLIBRC/matplotlibrc``
    - ``$MPLCONFIGDIR/matplotlibrc``
    - On Linux,
        - ``$XDG_CONFIG_HOME/matplotlib/matplotlibrc`` (if ``$XDG_CONFIG_HOME``
          is defined)
        - or ``$HOME/.config/matplotlib/matplotlibrc`` (if ``$XDG_CONFIG_HOME``
          is not defined)
    - On other platforms,
      - ``$HOME/.matplotlib/matplotlibrc`` if ``$HOME`` is defined
    - Lastly, it looks in ``$MATPLOTLIBDATA/matplotlibrc``, which should always
      exist.## Функция namedtuple
Сигнатура: `namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`
Returns a new subclass of tuple with named fields.

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)## Функция parse_version
Сигнатура: `parse(version: str) -> "Version"`
Parse the given version string.

    >>> parse('1.0.dev1')
    <Version('1.0.dev1')>

    :param version: The version string to parse.
    :raises InvalidVersion: When the version string is not a valid version.## Функция rc
Сигнатура: `rc(group, **kwargs)`
Set the current `.rcParams`.  *group* is the grouping for the rc, e.g.,
    for ``lines.linewidth`` the group is ``lines``, for
    ``axes.facecolor``, the group is ``axes``, and so on.  Group may
    also be a list or tuple of group names, e.g., (*xtick*, *ytick*).
    *kwargs* is a dictionary attribute name/value pairs, e.g.,::

      rc('lines', linewidth=2, color='r')

    sets the current `.rcParams` and is equivalent to::

      rcParams['lines.linewidth'] = 2
      rcParams['lines.color'] = 'r'

    The following aliases are available to save typing for interactive users:

    =====   =================
    Alias   Property
    =====   =================
    'lw'    'linewidth'
    'ls'    'linestyle'
    'c'     'color'
    'fc'    'facecolor'
    'ec'    'edgecolor'
    'mew'   'markeredgewidth'
    'aa'    'antialiased'
    =====   =================

    Thus you could abbreviate the above call as::

          rc('lines', lw=2, c='r')

    Note you can use python's kwargs dictionary facility to store
    dictionaries of default parameters.  e.g., you can customize the
    font rc as follows::

      font = {'family' : 'monospace',
              'weight' : 'bold',
              'size'   : 'larger'}
      rc('font', **font)  # pass in the font dict as kwargs

    This enables you to easily switch between several configurations.  Use
    ``matplotlib.style.use('default')`` or :func:`~matplotlib.rcdefaults` to
    restore the default `.rcParams` after changes.

    Notes
    -----
    Similar functionality is available by using the normal dict interface, i.e.
    ``rcParams.update({"lines.linewidth": 2, ...})`` (but ``rcParams.update``
    does not support abbreviations or grouping).## Функция rc_context
Сигнатура: `textlib.contextmanage`
Return a context manager for temporarily changing rcParams.

    The :rc:`backend` will not be reset by the context manager.

    rcParams changed both through the context manager invocation and
    in the body of the context will be reset on context exit.

    Parameters
    ----------
    rc : dict
        The rcParams to temporarily set.
    fname : str or path-like
        A file with Matplotlib rc settings. If both *fname* and *rc* are given,
        settings from *rc* take precedence.

    See Also
    --------
    :ref:`customizing-with-matplotlibrc-files`

    Examples
    --------
    Passing explicit values via a dict::

        with mpl.rc_context({'interactive': False}):
            fig, ax = plt.subplots()
            ax.plot(range(3), range(3))
            fig.savefig('example.png')
            plt.close(fig)

    Loading settings from a file::

         with mpl.rc_context(fname='print.rc'):
             plt.plot(x, y)  # uses 'print.rc'

    Setting in the context body::

        with mpl.rc_context():
            # will be reset
            mpl.rcParams['lines.linewidth'] = 5
            plt.plot(x, y)## Функция rc_file
Сигнатура: `rc_file(fname, *, use_default_template=True)`
Update `.rcParams` from file.

    Style-blacklisted `.rcParams` (defined in
    ``matplotlib.style.core.STYLE_BLACKLIST``) are not updated.

    Parameters
    ----------
    fname : str or path-like
        A file with Matplotlib rc settings.

    use_default_template : bool
        If True, initialize with default parameters before updating with those
        in the given file. If False, the current configuration persists
        and only the parameters specified in the file are updated.## Функция rc_file_defaults
Сигнатура: `rc_file_defaults()`
Restore the `.rcParams` from the original rc file loaded by Matplotlib.

    Style-blacklisted `.rcParams` (defined in
    ``matplotlib.style.core.STYLE_BLACKLIST``) are not updated.## Функция rc_params
Сигнатура: `rc_params(fail_on_error=False)`
Construct a `RcParams` instance from the default Matplotlib rc file.## Функция rc_params_from_file
Сигнатура: `rc_params_from_file(fname, fail_on_error=False, use_default_template=True)`
Construct a `RcParams` from file *fname*.

    Parameters
    ----------
    fname : str or path-like
        A file with Matplotlib rc settings.
    fail_on_error : bool
        If True, raise an error when the parser fails to convert a parameter.
    use_default_template : bool
        If True, initialize with default parameters before updating with those
        in the given file. If False, the configuration class only contains the
        parameters specified in the file. (Useful for updating dicts.)## Функция rcdefaults
Сигнатура: `rcdefaults()`
Restore the `.rcParams` from Matplotlib's internal default style.

    Style-blacklisted `.rcParams` (defined in
    ``matplotlib.style.core.STYLE_BLACKLIST``) are not updated.

    See Also
    --------
    matplotlib.rc_file_defaults
        Restore the `.rcParams` from the rc file originally loaded by
        Matplotlib.
    matplotlib.style.use
        Use a specific style file.  Call ``style.use('default')`` to restore
        the default style.## Функция sanitize_sequence
Сигнатура: `sanitize_sequence(data)`
Convert dictview objects to list. Other inputs are returned unchanged.## Функция set_loglevel
Сигнатура: `set_loglevel(level)`
Configure Matplotlib's logging levels.

    Matplotlib uses the standard library `logging` framework under the root
    logger 'matplotlib'.  This is a helper function to:

    - set Matplotlib's root logger level
    - set the root logger handler's level, creating the handler
      if it does not exist yet

    Typically, one should call ``set_loglevel("info")`` or
    ``set_loglevel("debug")`` to get additional debugging information.

    Users or applications that are installing their own logging handlers
    may want to directly manipulate ``logging.getLogger('matplotlib')`` rather
    than use this function.

    Parameters
    ----------
    level : {"notset", "debug", "info", "warning", "error", "critical"}
        The log level of the handler.

    Notes
    -----
    The first time this function is called, an additional handler is attached
    to Matplotlib's root handler; this handler is reused every time and this
    function simply manipulates the logger and handler's level.## Функция use
Сигнатура: `use(backend, *, force=True)`
Select the backend used for rendering and GUI integration.

    If pyplot is already imported, `~matplotlib.pyplot.switch_backend` is used
    and if the new backend is different than the current backend, all Figures
    will be closed.

    Parameters
    ----------
    backend : str
        The backend to switch to.  This can either be one of the standard
        backend names, which are case-insensitive:

        - interactive backends:
          GTK3Agg, GTK3Cairo, GTK4Agg, GTK4Cairo, MacOSX, nbAgg, QtAgg,
          QtCairo, TkAgg, TkCairo, WebAgg, WX, WXAgg, WXCairo, Qt5Agg, Qt5Cairo

        - non-interactive backends:
          agg, cairo, pdf, pgf, ps, svg, template

        or a string of the form: ``module://my.module.name``.

        Switching to an interactive backend is not possible if an unrelated
        event loop has already been started (e.g., switching to GTK3Agg if a
        TkAgg window has already been opened).  Switching to a non-interactive
        backend is always possible.

    force : bool, default: True
        If True (the default), raise an `ImportError` if the backend cannot be
        set up (either because it fails to import, or because an incompatible
        GUI interactive framework is already running); if False, silently
        ignore the failure.

    See Also
    --------
    :ref:`backends`
    matplotlib.get_backend
    matplotlib.pyplot.switch_backend