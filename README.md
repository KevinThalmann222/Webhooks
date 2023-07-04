# GitHub Actions: TeamsMessage-release

Dieses GitHub Actions-Workflow-Skript ermöglicht das Senden einer Teams-Nachricht, wenn ein Release veröffentlicht wird.

## Auslöser

Der Workflow wird ausgelöst durch:

Veröffentlichung eines Releases (`release: published`)
Manuelle Ausführung über den Workflow-Dispatch-Trigger (workflow_dispatch)

## Jobs

**build**
Dieser Job wird auf einem Ubuntu-Latest-Betriebssystem ausgeführt.

Schritte:

1. **Checkout des aktuellen Repositorys**: Das aktuelle Repository wird ausgecheckt.
2. **Python-Umgebung einrichten**: Die Python-Umgebung wird eingerichtet. Die gewünschte Python-Version wird angegeben.
3. **Installieren des Requests-Moduls**: Das Modul `pip install requests` wird installiert.
4. **Sende Teams-Nachricht**: Das Python-Skript "teams_webhook.py" wird mit den Release-Informationen als Argumente ausgeführt. Dieses Skript sendet eine Teams-Nachricht.

## Anmerkungen

- Das Skript verwendet das Modul "requests", daher wird dieses Modul vor der Ausführung installiert.
- Der Name und der Inhalt des veröffentlichten Releases werden als Argumente an das Python-Skript übergeben.
- Für die Verwendung von Geheimnissen (secrets) kann das entsprechende env-Block-Kommentar entfernt werden und das erforderliche Geheimnis in der Workflow-Konfiguration hinterlegt werden.

# GitHub Actions: TeamsMessage-push

Dieses GitHub Actions-Workflow-Skript ermöglicht das Senden einer Teams-Nachricht, wenn Code in den "master"-Branch gepusht wird.

## Auslöser

Der Workflow wird ausgelöst durch:

- Push in den "master"-Branch (`push: branches: [master]`)
- Manuelle Ausführung über den Workflow-Dispatch-Trigger (`workflow_dispatch`)

## Jobs

**build**
Dieser Job wird auf einem Ubuntu-Latest-Betriebssystem ausgeführt.

Schritte:

1. **Checkout des aktuellen Repositorys**: Das aktuelle Repository wird ausgecheckt.
2. **Python-Umgebung einrichten**: Die Python-Umgebung wird eingerichtet. Die gewünschte Python-Version wird angegeben.
3. **Installieren des Requests-Moduls**: Das Modul "requests" wird installiert.
4. **Sende Teams-Nachricht**: Das Python-Skript "teams_webhook.py" wird mit dem Argument "push" ausgeführt. Dieses Skript sendet eine Teams-Nachricht.

## Anmerkungen

- Das Skript verwendet das Modul "requests", daher wird dieses Modul vor der Ausführung installiert.
- Für die Verwendung von Geheimnissen (secrets) kann der entsprechende env-Block-Kommentar entfernt werden, und das erforderliche Geheimnis kann in der Workflow-Konfiguration hinterlegt werden.
  