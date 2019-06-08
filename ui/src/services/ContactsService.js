export default class ContactsService {

    constructor() {
        this._id = 4;
    }

    create(email, firstName, lastName) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                let newId = this._id ++;

                resolve({id: newId, email: email, firstName: firstName, lastName: lastName});

            }, 1000)
        })
    }

    loadAll() {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve([
                    {id: 1, email: 'jkowalski@gmail.com', firstName: 'Janek', lastName: 'Kowalski'},
                    {id: 2, email: 'mzdzblo@gmail.com', firstName: 'Mieciu', lastName: 'Źdźbło'},
                    {id: 3, email: 'awichura@gmail.com', firstName: 'Ania', lastName: 'Wichura'},
                ]);
            }, 1000)
        })
    }

    removeById(ids) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve();
            }, 1000)
        })
    }
}