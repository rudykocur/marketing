import { AbilityBuilder, Ability } from '@casl/ability'

export default function defineRightsFor(user) {
    const {rules, can, cannot} = AbilityBuilder.extract();

    if(user.role) {
        can(['view'], ['Logout']);
    }

    if (user.role === 'admin') {
        console.log('HELLO ADMIN');

        can(['view', 'manage'], ['Contacts', 'Groups', 'Templates', 'Mailing', 'Server']);
    } else if(user.role === 'agent') {
        console.log('HELLO AGENT');

        can(['view', 'manage'], ['Contacts', 'Groups']);
        can(['view'], ['Mailings', 'Templates']);
    } else if(user.role === 'user') {
        console.log('HELLO USER');

        can(['view', 'manage'], ['Contacts', 'Groups']);
        can(['view'], ['Mailings', 'Templates']);
    } else {
        console.log('HELLO ANON');
    }

    return new Ability(rules)
};