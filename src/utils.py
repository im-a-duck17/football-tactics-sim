def short_name(full_name):

    exceptions = {
        "Kevin De Bruyne": "De Bruyne",
        "Sergio Leonel Agüero del Castillo": "Agüero",
        "Fernando Luiz Rosa": "Fernandinho",
        "Fernando Francisco Reges": "Fernando",
        "Jesús Navas González": "Navas",
        "Nicolás Hernán Otamendi": "Otamendi",
        "Gaël Clichy": "Clichy",
        "Bacary Sagna": "Sagna",
        "Joe Hart": "Hart",
        "Kelechi Promise Iheanacho": "Iheanacho"
    }

    return exceptions.get(full_name, full_name.split()[-1])