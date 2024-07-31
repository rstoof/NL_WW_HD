import pytest
from src.data_fetcher import DataFetcher,CountryData

mock_data = [ {
  "id" : "3e37badc-d0f8-493e-a6d4-68ee7062cd5d",
  "type" : "reisadvies",
  "canonical" : "https://www.nederlandwereldwijd.nl/landen/frankrijk/reizen/reisadvies",
  "dataurl" : "https://opendata.nederlandwereldwijd.nl/v1/sources/nederlandwereldwijd/infotypes/traveladvice/3e37badc-d0f8-493e-a6d4-68ee7062cd5d",
  "title" : "Reisadvies Frankrijk | Ministerie van Buitenlandse Zaken",
  "introduction" : "<h2>In het kort</h2>\n   <ul>  <li>De Franse overheid schat de terrorismedreiging in het land\n    in als â€˜waarschijnlijkâ€™. Het alarmniveau is 3. Lees meer onder\n  Actueel.</li>  <li>De kleurcode van het reisadvies voor Frankrijk is\n    geel. U kunt erheen reizen. Maar let op: er zijn bijzondere\n  veiligheidsrisicoâ€™s.</li> </ul>\n   <div class=\"notification attention\">E-mail ontvangen als het\n  reisadvies wijzigt? <a\n    href=\"https://informatieservice.nederlandwereldwijd.nl/registration/simple\">Meld\n    u aan bij de Informatieservice</a>. Bent u in Frankrijk of gaat u\n  erheen? <a\n    href=\"https://informatieservice.nederlandwereldwijd.nl/registration/extended\">Registreer\n    uw verblijf</a>.</div>",
  "location" : "Frankrijk",
  "classification" : "Dit veld wordt niet meer ondersteund",
  "lastmodified" : "2024-07-26T12:02:00.000Z"
}]

@pytest.fixture
def fetcher(monkeypatch):
    fetcher = DataFetcher()
    monkeypatch.setattr(fetcher, 'fetch_data', lambda: fetcher.data.append(mock_data))
    fetcher.run()
    return fetcher

def test_get_data_urls(fetcher):
    assert fetcher.get_data_urls() == [mock_data[0]['dataurl']], "Data URLs do not match"

def test_dataframe_not_none(fetcher):
    assert fetcher.get_dataframe() is not None, "DataFrame is None"

def test_dataframe_not_empty(fetcher):
    df = fetcher.get_dataframe()
    assert not df.empty, "DataFrame is empty"

def test_dataframe_columns(fetcher):
    df = fetcher.get_dataframe()
    expected_columns = []  # Fill this with expected column names
    assert all(column in df.columns for column in expected_columns), "DataFrame does not contain expected columns"

@pytest.fixture
def country_data():
    return CountryData('France', mock_data[0]["dataurl"])

mock_country_data = {
  "id" : "3e37badc-d0f8-493e-a6d4-68ee7062cd5d",
  "type" : "reisadvies",
  "canonical" : "https://www.nederlandwereldwijd.nl/landen/frankrijk/reizen/reisadvies",
  "dataurl" : "https://opendata.nederlandwereldwijd.nl/v1/sources/nederlandwereldwijd/infotypes/traveladvice/3e37badc-d0f8-493e-a6d4-68ee7062cd5d",
  "title" : "Reisadvies Frankrijk | Ministerie van Buitenlandse Zaken",
  "introduction" : "<h2>In het kort</h2>\n   <ul>  <li>De Franse overheid schat de terrorismedreiging in het land\n    in als â€˜waarschijnlijkâ€™. Het alarmniveau is 3. Lees meer onder\n  Actueel.</li>  <li>De kleurcode van het reisadvies voor Frankrijk is\n    geel. U kunt erheen reizen. Maar let op: er zijn bijzondere\n  veiligheidsrisicoâ€™s.</li> </ul>\n   <div class=\"notification attention\">E-mail ontvangen als het\n  reisadvies wijzigt? <a\n    href=\"https://informatieservice.nederlandwereldwijd.nl/registration/simple\">Meld\n    u aan bij de Informatieservice</a>. Bent u in Frankrijk of gaat u\n  erheen? <a\n    href=\"https://informatieservice.nederlandwereldwijd.nl/registration/extended\">Registreer\n    uw verblijf</a>.</div>",
  "location" : "Frankrijk",
  "classification" : "Dit veld wordt niet meer ondersteund",
  "modificationdate" : "Laatst gewijzigd op: 29-07-2024 | Nog steeds geldig op: 31-07-2024",
  "modifications" : "Reist u naar Frankrijk? Lees welke veiligheidsrisicoâ€™s er zijn, wat u kunt doen in geval van nood, en hoe u zich voorbereidt op uw reis.",
  "content" : [ {
    "paragraph" : "https://opendata.nederlandwereldwijd.nl/documents/3432327/3734126/Reisadvies_Frankrijk_28-03-2024.png"
  }, {
    "paragraphtitle" : "Kaart bij reisadvies Frankrijk",
    "paragraph" : "<p><a href=\"https://opendata.nederlandwereldwijd.nl/documents/3432327/3734126/Reisadvies_Frankrijk_28-03-2024.pdf\">Download de kaart (PDF, 1393 kB)</a></p>"
  }, {
    "paragraphtitle" : "Actueel",
    "paragraph" : "<h4>Verhoogde terrorismedreiging</h4>\n   <p>Sinds 22 maart 2024 geldt in Frankrijk voor terrorismedreiging\n  alarmniveau 3 (het hoogste niveau). De Franse overheid schat de kans\n  op een terroristische aanslag op dit moment in als â€˜waarschijnlijkâ€™.\n  Dit geldt vooral voor de grotere steden.</p>\n   <p>U kunt naar Frankrijk reizen, maar wees alert. Volg de\n  aanwijzingen   van de Franse autoriteiten. <a\n    href=\"https://www.gouvernement.fr/actualite/plan-vigipirate-le-niveau-urgence-attentat-declare\">Lees\n    informatie over de veiligheidssituatie</a> op de website van de\n  Franse overheid (informatie in het Frans).</p>\n   <p>De Franse overheid gebruikt meer veiligheidsmaatregelen om burgers\n  te beschermen. Bijvoorbeeld bij musea, scholen, in het openbaar\n  vervoer, in warenhuizen en bij sportevenementen zoals\n  voetbalwedstrijden, de Olympische en Paralympische Spelen.</p>\n   <h4>Olympische en Paralympische Spelen</h4>\n   <p>De Olympische Spelen zijn van 26 juli tot en met 11 augustus 2024\n  in Parijs en andere steden in Frankrijk. De Paralympische Spelen\n  vinden plaats van 28 augustus tot en met 8 september 2024.</p>\n   <ul>  <li>U heeft een digitale pas (Pass Jeux) nodig om naar bepaalde\n    delen van Parijs te reizen. <a\n      href=\"https://anticiperlesjeux.gouv.fr/en/je-minforme/pass-jeux-etes-vous-concerne\">Lees\n      meer informatie op de website van de Franse overheid</a>\n    (informatie in het Frans en Engels).</li>  <li>Zorg dat u altijd een\n    geldig paspoort of geldige ID-kaart bij u heeft. Let op uw omgeving\n    en uw spullen en volg de aanwijzingen van de lokale\n  autoriteiten.</li>  <li>     <a\n      href=\"https://www.rijksoverheid.nl/ministeries/ministerie-van-buitenlandse-zaken/het-werk-van-bz-in-de-praktijk/weblogs/2023/spelen-in-parijs-10-tips-jan-versteeg\">Lees\n      de tips van de Nederlandse ambassadeur in Parijs</a> op\n  Rijksoverheid.nl.</li> </ul>"
  }, {
    "paragraphtitle" : "Terrorisme",
    "paragraph" : "<p>Sinds 22 maart 2024 geldt in Frankrijk voor terrorismedreiging\n  alarmniveau 3 (het hoogste niveau). Dit geldt vooral voor de grotere\n  steden. In 2023 hebben in Frankrijk 2 aanslagen met dodelijke afloop\n  plaatsgevonden, in Arras en Parijs.</p>\n          <p>Houd in heel Frankrijk rekening met de verhoogde kans op\n  een   terroristische aanslag.</p>\n          <ul>  <li>Wees in heel Frankrijk extra waakzaam, zeker op\n    plaatsen     waar veel mensen zijn.</li>  <li>Houd rekening met\n    extra     veiligheidsmaatregelen bij grote culturele en\n  sportevenementen.</li>     <li>Musea, monumenten en andere publieke\n    locaties kunnen worden     ontruimd bij een dreiging. Bijvoorbeeld\n    bij achtergelaten bagage of     verdachte pakketten.</li>  <li>De\n    Franse autoriteiten voeren     verscherpte (identiteits-)controles\n    uit. Werk daar altijd aan   mee.</li>  <li>Volg altijd de\n    aanwijzingen van de Franse   autoriteiten.</li>  <li>Blijf voor en\n    tijdens uw reis op de hoogte van     de actuele situatie en de extra\n  veiligheidsmaatregelen.Â </li>     <li>Volg het lokale nieuws.</li>\n    <li>     <a\n      href=\"https://www.gouvernement.fr/reagir-attaque-terroriste\">Lees\n      wat u kunt doen bij een terroristische aanslag</a> op de website\n    van de Franse overheid (informatie in het Frans).</li> </ul>"
  }, {
    "paragraphtitle" : "Criminaliteit",
    "paragraph" : "<p>In Frankrijk komt criminaliteit voor. Vooral in grote steden als\n  Parijs, Marseille en Lyon. Houd rekening met zakkenrollers en\n  diefstal, vooral op drukke plekken. Bezoek geen afgelegen straten,\n  wijken of parken.</p>\n    <p>Door een goede voorbereiding verkleint u de kans dat u wordt\n  beroofd of opgelicht. Lees meer op de pagina <a\n    href=\"https://www.nederlandwereldwijd.nl/reisadvies/criminaliteit\">Hoe\n    voorkom ik dat ik slachtoffer word van criminaliteit in het buitenland?</a></p>"
  }, {
    "paragraphtitle" : "Wetten en gebruiken",
    "paragraph" : "<h4>Drugs</h4>\n          <p>U mag in Frankrijk geen drugs gebruiken, bezitten of\n  verkopen.   Dit   geldt ook voor softdrugs. In Frankrijk zijn straffen\n  veel   zwaarder dan   in Nederland.</p>\n          <h4>Identificatieplicht</h4>\n          <p>In Frankrijk bent u strafbaar als u zich niet kunt\n  identificeren   met een geldig paspoort of geldige ID-kaart.</p>"
  }, {
    "paragraphtitle" : "Natuurgeweld",
    "paragraph" : "<h4>Bosbranden</h4>\n          <p>In Frankrijk en op het eiland Corsica komen bosbranden\n  voor.   Vooral   in de zomer als het lang droog is. <a\n    href=\"https://meteofrance.com/meteo-des-forets\">Lees meer over\n    bosbrandgevaar in Frankrijk</a> op de website van MÃ©tÃ©o des forÃªts\n  (informatie in het Frans). </p>\n          <p>Bekijk het actuele risico op bosbranden voor de Franse\n  departementen waar de kans op bosbranden het grootst is op de websites\n  van de Franse overheid (informatie in het Frans):</p>\n          <ul>  <li>     <a\n  href=\"https://www.risque-prevention-incendie.fr/corse/\">Corsica</a></li>\n    <li>     <a\n  href=\"https://www.risque-prevention-incendie.fr/var/\">Var</a></li> </ul>\n          <h4>Lawines</h4>\n          <p>Er is een hoog risico op lawines in de winter, vooral als u\n  gaat   skiÃ«n of snowboarden buiten de officiÃ«le skipistes (off-piste).\n    <a\n    href=\"https://www.avalanches.org/standards/avalanche-danger-scale/\">Lees\n    meer over lawines</a> op de website van de European Avalanche\n  Warning Services (informatie in het Engels).</p>"
  }, {
    "paragraphtitle" : "Demonstraties",
    "paragraph" : "<p>In Frankrijk zijn regelmatig demonstraties. Vooral in de grotere\n  steden, en op en rond belangrijke verkeerswegen en pleinen. Daarbij\n  kan geweld ontstaan. Vermijd samenscholingen, mensenmassaâ€™s en\n  demonstraties. Volg het nieuws via de (lokale) media. Of vraag bij uw\n  hotel om informatie.</p>"
  }, {
    "paragraphtitle" : "In geval van nood",
    "paragraph" : "<h4>Lokale hulpdiensten</h4>\n          <p>Heeft u direct hulp nodig in Frankrijk? Neem contact op met\n  de   lokale hulpdiensten:</p>\n          <ul>  <li>Algemeen alarmnummer (politie): 112</li>\n    <li>Ambulance:   15</li>  <li>Brandweer: 18</li> </ul>\n          <h4>Nood- of crisissituatie</h4>\n          <ul>  <li>Bent u in Frankrijk en bent u in nood? Bijvoorbeeld:\n    u     bent     opgenomen in het ziekenhuis, of u bent bestolen. <a\n      href=\"https://www.nederlandwereldwijd.nl/hulp-bij-nood\">Lees wat u\n      kunt doen in geval van nood</a>. </li>  <li>Komt u in een\n    crisissituatie terecht (zoals politieke onrust, een terroristische\n    aanslag of natuurgeweld)? <a\n      href=\"https://www.nederlandwereldwijd.nl/crisis/regelen-in-crisissituatie\">Lees\n      wat u kunt doen in een crisissituatie</a>.</li>  <li>Laat uw\n    familie/vrienden weten hoe het met u gaat. </li>  <li>Volg altijd de\n    aanwijzingen op van de lokale autoriteiten. </li>  <li>Maakt u een\n    georganiseerde reis? Houd contact met uw reisorganisatie. </li>\n    <li>Heeft u hulp nodig? Neem contact op met uw reisverzekeraar of\n    met de Nederlandse ambassade.</li> </ul>\n          <h4>Contactgegevens Nederlandse ambassade in geval van nood</h4>\n          <p>Nederlandse ambassades en consulaten-generaal zijn 24 uur\n  per   dag,   7 dagen per week bereikbaar via het contactcenter van\n  NederlandWereldwijd op telefoonnummer <a\n    href=\"tel:+31-247-247-247\">+31 247 247 247</a> of via WhatsApp: <a\n    href=\"https://wa.me/31682387796\">+31 6 82 38 77 96</a>.</p>\n          <h4>Nederlandse ambassade in Frankrijk</h4>\n          <p>Bekijk de contactgegevens van de <a\n    href=\"https://www.nederlandwereldwijd.nl/contact/ambassades-consulaten-generaal/frankrijk/ambassade-parijs\">contactgegevens\n    van de Nederlandse ambassade in Parijs</a>.</p>"
  }, {
    "paragraphtitle" : "Reisverzekering",
    "paragraph" : "<ul>  <li>Sluit altijd een goede reisverzekering af die de extra kosten\n    dekt van bijvoorbeeld ziekenhuisopname, of als u naar Nederland moet\n    worden vervoerd (repatriÃ«ring). Uw basiszorgverzekering vergoedt\n    deze kosten niet altijd 100 procent.</li>  <li>Gaat u een (extreme)\n    sport beoefenen? Sluit een extra verzekering af.</li> </ul>"
  }, {
    "paragraphtitle" : "Paspoort, ID-kaart, rijbewijs",
    "paragraph" : "<h4>Paspoort of ID-kaart</h4>\n              <ul>  <li>U heeft een geldig paspoort of geldige ID-kaart\n    nodig     om     naar Frankrijk te reizen.</li>  <li>Uw Nederlandse\n    paspoort     of     ID-kaart moet nog geldig zijn op het moment van\n    vertrek uit     het   land.</li> </ul>\n              <h4>Visum</h4>\n              <p>U heeft geen visum nodig voor Frankrijk als u met een\n  Nederlands   paspoort of Nederlandse ID-kaart reist.</p>\n              <h4>Reizen met kinderen</h4>\n              <p>Kinderen hebben ook een geldig paspoort of geldige\n  ID-kaart   nodig   voor een reis naar Frankrijk. Reist u alleen met 1\n  of meer   kinderen   jonger dan 18 jaar? <a\n    href=\"https://www.rijksoverheid.nl/documenten/formulieren/2014/02/06/formulier-toestemming-reizen-met-minderjarige-naar-het-buitenland\">Check\n    welke documenten u nodig heeft om te reizen met een minderjarig\n  kind</a> en neem die mee. Zo voorkomt u problemen en lange wachttijden\n  bij grenscontroles.</p>\n              <h4>Rijbewijs</h4>\n              <p>Uw Nederlandse rijbewijs is geldig in Frankrijk. <a\n    href=\"https://www.anwb.nl/vakantie/frankrijk/reisvoorbereiding\">Lees\n    meer over rijden in Frankrijk</a> (onder andere over milieustickers)\n  op de website van de ANWB.</p>"
  }, {
    "paragraphtitle" : "Reisvaccinaties",
    "paragraph" : "<ul>  <li>Voor Frankrijk heeft u geen vaccinaties nodig. <a\n      href=\"https://www.ggdreisvaccinaties.nl/land/frankrijk\">Check de\n      adviezen voor Frankrijk</a> op de website van GGD\n  Reisvaccinaties.</li>  <li>Maak (online) een vaccinatie-afspraak bij\n    een GGD of andere aanbieder van reisvaccinaties bij u in de buurt.\n      <a href=\"https://www.lcr.nl/Vaccinatie-adressen\">Check alle\n      aanbieders van reisvaccinaties</a> op de website van het Landelijk\n    CoÃ¶rdinatiecentrum Reizigersadvisering (LCR).</li> </ul>"
  }, {
    "paragraphtitle" : "Medicijnen",
    "paragraph" : "<p>Gebruikt u medicijnen?</p>\n              <ul>  <li>Neem voldoende medicijnen mee, ook voor extra\n  dagen.</li>     <li>     <a\n      href=\"https://www.hetcak.nl/regelingen/medicijnen-mee-op-reis\">Check\n      of u een medicijnverklaring nodig heeft</a> om uw medicijnen mee\n    te mogen nemen naar Frankrijk.</li>  <li>Neem de medicijnen altijd\n    mee in de originele verpakking.</li> </ul>"
  }, {
    "paragraphtitle" : "Bagageregels",
    "paragraph" : "<h4>Wat mag ik meenemen naar Frankrijk?</h4>\n              <p>   <a\n    href=\"https://www.iatatravelcentre.com/FR-France-customs-currency-airport-tax-regulations-summary.htm\">Check\n    wat u mag meenemen naar Frankrijk</a> op de website van IATA\n  (informatie in het Engels).</p>\n              <h4>Wat mag ik mee terugnemen naar Nederland?</h4>\n              <p>Bekijk wat u vanuit Frankrijk mee terug mag nemen naar\n  Nederland   op   de pagina <a\n    href=\"https://www.nederlandwereldwijd.nl/reizen-naar-nederland/meenemen-nederland\">Wat\n    mag ik meenemen naar Nederland?</a></p>"
  } ],
  "authorities" : [ "Ministerie van Buitenlandse Zaken" ],
  "creators" : [ "Ministerie van Buitenlandse Zaken" ],
  "lastmodified" : "2024-07-26T12:02:00.000Z",
  "issued" : "2012-08-28T10:38:00.000Z",
  "available" : "2012-08-28T10:38:00.000Z",
  "license" : "CC0 1.0 Universal",
  "rightsholders" : [ "Ministerie van Buitenlandse Zaken" ],
  "language" : "nl",
  "subject" : " ",
  "themes" : [ ]
}

def test_get_dataurl_contents(country_data,requests_mock):
    requests_mock.get(country_data.dataurl, json=mock_country_data)
    assert country_data.get_dataurl_contents() == mock_country_data, "Dataframe does not match"

def test_get_map_pdf_url(country_data):
    country_data.json = mock_country_data
    assert country_data.get_map_pdf_url() == "https://opendata.nederlandwereldwijd.nl/documents/3432327/3734126/Reisadvies_Frankrijk_28-03-2024.pdf", "Map PDF URL does not match"