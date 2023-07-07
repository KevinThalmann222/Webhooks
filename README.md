# Sub-Module einbinden

01. Navigiere zum Hauptverzeichnis deines Repositories in der Befehlszeile oder im Terminal.
02. Führe den folgenden Befehl aus, um das Submodul hinzuzufügen:
03. `git submodule add **Submodul-URL** **Pfad im Hauptrepository**`
04. Ersetze `Submodul-URL` durch die URL des Submoduls, das du einbinden möchtest, und `Pfad im Hauptrepository` durch den Pfad, unter dem das Submodul in deinem Hauptrepository erscheinen soll.
05. z.B. `git submodule add https://github.com/KevinThalmann222/WorkSpacePython.git Webhooks\Submodul` oder
06. `git submodule add https://github.com/KevinThalmann222/WorkSpacePython.git`
07. Erstelle die Datei **.gitmodules** und füge folgenede Zeilen hinzu:
08. Inhalt **.gitmodules**
   - [submodule "WorkSpacePython"]
   - path = WorkSpacePython
   - url = `https://github.com/KevinThalmann222/WorkSpacePython.git`
09. Führe den Befehl `git submodule init` aus, um das Submodul zu initialisieren.
10. Führe den Befehl `git submodule update` aus, um das Submodul herunterzuladen und in deinem Hauptrepository zu speichern.
11. Git update submodule `git submodule update --remote <Name_submodule>` bzw. `git submodule update --remote WorkSpacePython`

## GitHub Actions: TeamsMessage-release

Dieses GitHub Actions-Workflow-Skript ermöglicht das Senden einer Teams-Nachricht, wenn ein Release veröffentlicht wird.

## Auslöser1

Der Workflow wird ausgelöst durch:

Veröffentlichung eines Releases (`release: published`)
Manuelle Ausführung über den Workflow-Dispatch-Trigger (workflow_dispatch)

## Jobs1

**build**
Dieser Job wird auf einem Ubuntu-Latest-Betriebssystem ausgeführt.

Schritte:

1. **Checkout des aktuellen Repositorys**: Das aktuelle Repository wird ausgecheckt.
2. **Python-Umgebung einrichten**: Die Python-Umgebung wird eingerichtet. Die gewünschte Python-Version wird angegeben.
3. **Installieren des Requests-Moduls**: Das Modul `pip install requests` wird installiert.
4. **Sende Teams-Nachricht**: Das Python-Skript "teams_webhook.py" wird mit den Release-Informationen als Argumente ausgeführt. Dieses Skript sendet eine Teams-Nachricht.

## Anmerkungen1

- Das Skript verwendet das Modul "requests", daher wird dieses Modul vor der Ausführung installiert.
- Der Name und der Inhalt des veröffentlichten Releases werden als Argumente an das Python-Skript übergeben.
- Für die Verwendung von Geheimnissen (secrets) kann das entsprechende env-Block-Kommentar entfernt werden und das erforderliche Geheimnis in der Workflow-Konfiguration hinterlegt werden.

## GitHub Actions: TeamsMessage-push

Dieses GitHub Actions-Workflow-Skript ermöglicht das Senden einer Teams-Nachricht, wenn Code in den "master"-Branch gepusht wird.

## Auslöser2

Der Workflow wird ausgelöst durch:

- Push in den "master"-Branch (`push: branches: [master]`)
- Manuelle Ausführung über den Workflow-Dispatch-Trigger (`workflow_dispatch`)

## Jobs2

**build**
Dieser Job wird auf einem Ubuntu-Latest-Betriebssystem ausgeführt.

Schritte:

1. **Checkout des aktuellen Repositorys**: Das aktuelle Repository wird ausgecheckt.
2. **Python-Umgebung einrichten**: Die Python-Umgebung wird eingerichtet. Die gewünschte Python-Version wird angegeben.
3. **Installieren des Requests-Moduls**: Das Modul "requests" wird installiert.
4. **Sende Teams-Nachricht**: Das Python-Skript "teams_webhook.py" wird mit dem Argument "push" ausgeführt. Dieses Skript sendet eine Teams-Nachricht.

## Anmerkunge2

- Das Skript verwendet das Modul "requests", daher wird dieses Modul vor der Ausführung installiert.
- Für die Verwendung von Geheimnissen (secrets) kann der entsprechende env-Block-Kommentar entfernt werden, und das erforderliche Geheimnis kann in der Workflow-Konfiguration hinterlegt werden.
