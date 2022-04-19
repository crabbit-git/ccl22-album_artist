from flask import Flask, render_template, redirect
from flask import Blueprint
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)

