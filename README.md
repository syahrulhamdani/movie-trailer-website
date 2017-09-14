# Movie Trailer Website

Create a movie trailer website generated from a python file

## Getting Started

* To start up, please make sure that all these python files `media.py`,
`entertainment_center.py`, and `fresh_tomatoes.py` are in the same folder.

* Simply run the constructor `entertainment_center.py` to generate the website.

* You will find an HTML file related to `fresh_tomatoes.py` that you have
created from running the `entertainment_center.py`

## Usage

The HTML file that has created is generated from `fresh_tomatoes.py` and can be
modified as you wish.

There are 3 section available in `fresh_tomatoes.py` that stands for the HTML
and you can edit:

```python
main_page_head = """ ... """
```
```python
main_page_content = """ ... """
```
```python
movie_tile_content = """ ... """
```
If you want to add more movies, you can add it in
`entertainment_center.py` file below  `instatiate part`, there will be comments
to make you easier to edit.

Don't forget to push it into the `movies_list` list as mentioned below without
the quotation marks

```python
movies_list = [spiderman, avenger, minions, despicable_me_2, boss_baby,
                sherlock_holmes, percy_jackson, "your additional movie"]
```

## How to

You can run the program by following short instruction in `Getting Started`
part, or using windows `command prompt` (if you use windows) explained below.
But first, for simplicity reason, place the 3 files inside a folder named
`Movie Trailer Website` in your desktop.

1. Open windows `command prompt`.
2. If you don't know how, simply <kbd>win</kbd> + <kbd>r</kbd>, then type
`cmd`, then press `enter`.
3. After the `command prompt` is opened, prompt
`cd desktop/Movie Trailer Website`.
4. Then, prompt `python entertainment_center.py`.
5. You will get directly into your browser and see the result.

### Notes

Before you do the previous instruction, make sure that your `python` file has
been added to your PATH. if it doesn't, you can follow the instruction provided [here](https://www.google.co.id/search?q=how+to+add+python+to+path+on+windows&oq=how+to+add+python+to+path+on+windows&gs_l=psy-ab.3..0i19k1l2j0i22i30i19k1l2.12592.13846.0.14662.11.7.0.0.0.0.732.1148.4-1j0j1.2.0....0...1.1.64.psy-ab..9.2.1147.RcHHhFtlvUc) based on your OS
