"""Enum type definitions."""

from enum import Enum

__all__ = ["MediaType", "MessageType", "ProviderType", "SettingType"]


class MediaType(Enum):
    EPISODE = "episode"
    MOVIE = "movie"


class MessageType(Enum):
    INFO = None
    ALERT = "yellow"
    ERROR = "red"
    SUCCESS = "green"
    HEADING = "bold"


class ProviderType(Enum):
    TVDB = "tvdb"
    TVMAZE = "tvmaze"
    TMDB = "tmdb"
    OMDB = "omdb"


class RelocateType(Enum):
    DEFAULT = "move"
    HARDLINK = "hard"
    SYMBOLICLINK = "sym"
    COPY = "copy"


class SettingType(Enum):
    DIRECTIVE = "directive"
    PARAMETER = "parameter"
    POSITIONAL = "positional"
    CONFIGURATION = "configuration"
