

export default class SettingsService {
    load() {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve({
                    address: 'https://api.flypsdm.io/public/api/v1',
                    password: 'teset',
                    fromName: 'Jan Kowalski',
                    fromAddress: 'jkowalski@gmail.com',
                });
            }, 2000)
        })
    }

    save(newSettings) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve();
            }, 2000)
        })
    }
}