[![](https://img.shields.io/badge/naobito_1.0.0-passing-green)](https://github.com/gongahkia/naobito/releases/tag/1.0.0) 

# `Naobito`

A simple Web App that creates Wallpapers from your [Manga](https://en.wikipedia.org/wiki/Manga) and [Comics](https://en.wikipedia.org/wiki/Comics).

Cooked up in [2.5 hours]() to take a break from [finals studying](./asset/reference/finals.jpg).

<div style="display: flex; align-items: center; justify-content: center; gap: 2rem;">
  <div style="flex: none;">
    <img 
      src="./asset/reference/example.jpg" 
      alt="Full Manga Panel" 
      style="display: block; max-width: 400px; width: 100%; height: auto; box-shadow: 0 4px 16px rgba(0,0,0,0.15);"
    >
  </div>
  <div style="flex: none; display: flex; align-items: center; justify-content: center;">
    <svg width="48" height="48" viewBox="0 0 48 48">
      <polygon points="16,8 40,24 16,40" fill="#333"/>
    </svg>
  </div>
  <div style="display: flex; flex-direction: column; gap: 0.5rem; align-items: flex-start;">
    <img src="./asset/reference/panel_1.png" alt="Panel 1" style="display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.10); background: #fff;">
    <img src="./asset/reference/panel_2.png" alt="Panel 2" style="display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.10); background: #fff;">
    <img src="./asset/reference/panel_3.png" alt="Panel 3" style="display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.10); background: #fff;">
    <img src="./asset/reference/panel_4.png" alt="Panel 4" style="display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.10); background: #fff;">
    <img src="./asset/reference/panel_5.png" alt="Panel 5" style="display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.10); background: #fff;">
  </div>
</div>


## Stack

* *Frontend*: React, JavaScript
* *Backend*: Flask, Python

## Usage

Host `Naobito` locally by running the below.

```console
$ git clone https://github.com/gongahkia/naobito
$ cd naobito
$ sudo apt install graphviz
$ python3 -m venv myenv
$ pip install opencv-python numpy flask flask-cors opencv-python numpy diagrams
$ cd naobito-app
$ npm install axios
$ cd ..
$ python3 main.py
```

Then access the frontend at [localhost:3000](http://localhost:3000) and *(optionally)* the backend at [localhost:5000](http://localhost:5000).

## Architecture

![](./asset/reference/architecture.png)

## References

The name `Naobito` is in reference to [Naobito Zenin](https://jujutsu-kaisen.fandom.com/wiki/Naobito_Zenin), a [Special Grade 1](https://jujutsu-kaisen.fandom.com/wiki/Grade) [Jujutsu Sorcerer](https://jujutsu-kaisen.fandom.com/wiki/Jujutsu_Sorcerer) and the 26th head of the [Zenin Clan](https://jujutsu-kaisen.fandom.com/wiki/Sorcerer_Clan/Zenin_Clan). Naobito first makes an appearance in the [Shibuya Incident arc](https://jujutsu-kaisen.fandom.com/wiki/Shibuya_Incident_Arc) of the manga series [Jujutsu Kaisen](https://jujutsu-kaisen.fandom.com/wiki/Jujutsu_Kaisen_Wiki).

<div align="center">
    <img src="./asset/logo/naobito.jpg" width="75%"></img>
</div>