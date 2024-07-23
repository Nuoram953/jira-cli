#!/usr/bin/env python3

import click
import inquirer

@click.group()
def cli():
    """CLI tool with multiple commands"""
    pass

@cli.command()
@click.option("--id", help="Id of the ticket")
@click.option("--parent", default=None, help="")
@click.option("--who", default="me", help="Who is the assignee")
@click.option("--creation", default="me", help="Creation date")
@click.option("--type", default=None, help="Tpye of the ticket")
def view_tickets(id, parent, who, creation, type):
    raise NotImplementedError("WIP")

@cli.command()
@click.option("--id", help="Id of the ticket")
def view_ticket(id, parent, who, creation, type):
    raise NotImplementedError("WIP")

@cli.command()
@click.option("--id", help="Id of the ticket")
def create_ticket(id, parent, who, creation, type):
    raise NotImplementedError("WIP")

@cli.command()
@click.option("--id", help="Id of the ticket")
def update_ticket(id, parent, who, creation, type):
    raise NotImplementedError("WIP")

@cli.command()
@click.option("--id", help="Id of the ticket")
@click.option("--time", help="Id of the ticket")
@click.option("--comment", help="What did you work on?")
def add_worklog(id, parent, who, creation, type):
    raise NotImplementedError("WIP")

@cli.command()
@click.option("--id", help="Id of the ticket")
def move_issue(id, parent, who, creation, type):
    raise NotImplementedError("WIP")

@cli.command()
@click.option("--id", help="Id of the ticket")
def clone_issue(id, parent, who, creation, type):
    raise NotImplementedError("WIP")

@cli.command()
@click.option("--id", help="Id of the ticket")
def search_issues(id, parent, who, creation, type):
    raise NotImplementedError("WIP")

if __name__ == '__main__':
    cli()
