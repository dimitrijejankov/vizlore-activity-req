from sklearn.externals import joblib


class ClassifierLoader:

    svc_acc_gyo = None
    svc_acc = None
    tree_acc_gyo = None
    tree_acc = None

    svc_acc_gyo_ech = None
    svc_acc_ech = None
    tree_acc_gyo_ech = None
    tree_acc_ech = None

    def __init__(self):
        self.svc_acc_gyo = joblib.load('./activity_server/classifier/acc_gyo/classifier_svc.pkl')
        self.svc_acc = joblib.load('./activity_server/classifier/acc/classifier_svc.pkl')
        self.svc_acc_gyo_ech = joblib.load('./activity_server/classifier/acc_gyo_ech/classifier_svc.pkl')
        self.svc_acc_ech = joblib.load('./activity_server/classifier/acc_ech/classifier_svc.pkl')

        self.tree_acc_gyo = joblib.load('./activity_server/classifier/acc_gyo/classifier_tree.pkl')
        self.tree_acc = joblib.load('./activity_server/classifier/acc/classifier_tree.pkl')
        self.tree_acc_gyo_ech = joblib.load('./activity_server/classifier/acc_gyo_ech/classifier_tree.pkl')
        self.tree_acc_ech = joblib.load('./activity_server/classifier/acc_ech/classifier_tree.pkl')

    def get_classifier(self, classifier, data, features):
        if classifier == 'svc' and data == 'acc' and features == 'std':
            return self.svc_acc
        elif classifier == 'svc' and data == 'acc_gyo' and features == 'std':
            return self.svc_acc_gyo
        elif classifier == 'svc' and data == 'acc' and features == 'ech':
            return self.svc_acc_ech
        elif classifier == 'svc' and data == 'acc_gyo' and features == 'ech':
            return self.svc_acc_gyo_ech
        elif classifier == 'dt' and data == 'acc' and features == 'std':
            return self.tree_acc
        elif classifier == 'dt' and data == 'acc_gyo' and features == 'std':
            return self.tree_acc_gyo
        elif classifier == 'dt' and data == 'acc' and features == 'ech':
            return self.tree_acc_ech
        elif classifier == 'dt' and data == 'acc_gyo' and features == 'ech':
            return self.tree_acc_gyo_ech
