import { AbilityBuilder, Ability } from '@casl/ability'

export default function defineRightsFor(user) {
    const {rules, can, cannot} = AbilityBuilder.extract();

    if(user.role) {
        can(['view'], ['Logout']);
    }

    if (user.role === 'admin') {
        can(['view', 'manage'], ['Contacts', 'Groups', 'Templates', 'Mailing', 'Server']);

    } else if(user.role === 'agent') {
        can(['view', 'manage'], ['Contacts', 'Groups']);
        can(['view'], ['Mailing', 'Templates']);

    } else if(user.role === 'user') {
        can(['view'], ['Contacts', 'Groups', 'Mailing', 'Templates']);

    }

    return new Ability(rules)
};