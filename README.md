# easyi3status maildir module

Demo:  
![demo](https://image.ibb.co/gS0iKQ/output_ag_TFLa.gif) ![demo2](https://image.ibb.co/iLuqYk/small2.png)

## To Install

    wget https://raw.githubusercontent.com/aecepoglu/easyi3status-maildir/master/maildir.py -P ~/.config/easyi3status/modules/
    wget https://raw.githubusercontent.com/aecepoglu/easyi3status-maildir/master/config.yaml -O - >> ~/.config/easyi3status/config.yaml

### Set maildir path

Open `~/.config/easyi3status/config.yaml` and set your maildir path

```yaml
- name: maildir
  config:
    path: /home/aecepoglu/mail/inbox #set this to point to a maildir directory
```

And restart i3 for the changes to take effect.

## Configuration

* `path`: path to a maildir folder. **REQUIRED**. It expects there to be a folder with maildir structure (with *cur, new, tmp* folders at given path) 
* `label`: optional label
* `hideCount`: hides the count from the display. `true` or `false`. Defaults to `false`
* `hideIfZero`: show nothing if the count is 0. `true` or `false`. Defaults to `false`
