from fastapi import FastAPI;

portfolio = FastAPI()

@portfolio.get('/',description='This is root route')
def root():
    return("Root directory")

