#!/usr/bin/env python3

import click
import inquirer

from constant import Option, ErrorMessage


@click.group()
def cli():
    """CLI tool with multiple commands"""
    pass


@cli.command()
@click.option(
    Option.SPRINT.full(), is_flag=True, default=False, help=Option.SPRINT.help()
)
@click.option(
    Option.PARENT.short(), Option.PARENT.full(), default=None, help=Option.PARENT.help()
)
@click.option("--who", default="me", help="Who is the assignee")
@click.option("--creation", default="me", help="Creation date")
@click.option("--type", default=None, help="Tpye of the issue")
def view_issues(sprint, parent, who, creation, type):
    raise NotImplementedError(ErrorMessage.WIP.value)


@cli.command()
@click.option(Option.ID.full(), help=Option.ID.help())
@click.option("--web", default=False, help="Open the issue in your default browser")
def view_issue(id, web):
    raise NotImplementedError(ErrorMessage.WIP.value)


@cli.command()
@click.option(Option.ID.full(), help=Option.ID.help())
def create_issue(id):
    raise NotImplementedError(ErrorMessage.WIP.value)


@cli.command()
@click.option(Option.ID.full(), help=Option.ID.help())
def update_issue(id):
    raise NotImplementedError(ErrorMessage.WIP.value)


@cli.command()
@click.option(Option.ID.full(), help=Option.ID.help())
@click.option("--time", help="Id of the issue")
@click.option("--comment", help="What did you work on?")
@click.option("--date", help="What did you work on?")
def add_worklog(id, time, comment, date):
    raise NotImplementedError(ErrorMessage.WIP.value)


@cli.command()
@click.option(Option.ID.full(), help=Option.ID.help())
def move_issue(id):
    raise NotImplementedError(ErrorMessage.WIP.value)


@cli.command()
@click.option(Option.ID.full(), help=Option.ID.help())
def clone_issue(id):
    raise NotImplementedError(ErrorMessage.WIP.value)


@cli.command()
@click.option(Option.ID.full(), help=Option.ID.help())
def search_issues(id):
    raise NotImplementedError(ErrorMessage.WIP.value)


@cli.command()
@click.option(Option.ID.full(), help=Option.ID.help())
@click.option("--message", help="Id of the issue")
@click.option("--ping", default=False, help="Add a ping")
def add_comment(id, message, ping):
    raise NotImplementedError(ErrorMessage.WIP.value)


if __name__ == "__main__":
    cli()
