const database = 'voice-controlled-secretary';
const collection = 'apiKeys';

use(database);

db.createCollection(collection)


db.apiKeys.insertMany([
    { 'model_api_key' : 'AIzaSyCuWMPanIsa1PB3HYw3EV6vOsfgfL8IuiU' },
    { 'deepgram_api_key': 'a6349ec3e22ab04bec3aad586a3775fa0f76721e' }
])