from watson_developer_cloud import AssistantV1


class Watson:
    def __init__(self, watson_key, workspace_id):
        self.workspace_id = workspace_id
        self.agent = AssistantV1("2019-03-23", iam_apikey=watson_key)

    def messsage(self, text, context=None):
        input = {"text": text}

        r = self.agent.message(
            workspace_id=self.workspace_id, input=input, context=context)

        return r.get_result()

