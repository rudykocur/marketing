export default class TemplatesService {
    constructor() {
        this._id = 4;
    }

    create(name, content) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve({id: this._id++, name: name, content: content});
            }, 1000)
        })
    }

    loadAll() {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve([
                    {id: 1, name: 'Welcome email', content: 'Welcome mail content!'},
                    {id: 2, name: 'New exciting product in store', content: 'We would like to introduce brand new ...'},
                    {id: 3, name: 'Obligatory lipsum', content: 'Lorem ipsum dolor sit amet'},
                ]);
            }, 1000)
        })
    }
}