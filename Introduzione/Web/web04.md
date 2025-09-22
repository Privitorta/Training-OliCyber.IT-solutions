`curl http://web-04.challs.olicyber.it/users`

```
{
  "users": [
    {
      "name": "admin",
      "role": "admin",
      "registration_date": "2018-06-18T15:34:55Z"
    },
    {
      "name": "fruitfly",
      "role": "user",
      "registration_date": "2019-08-12T12:04:32Z"
    },
    {
      "name": "jim87",
      "role": "user",
      "registration_date": "2022-01-13T20:09:43Z"
    },
    {
      "name": "anonymous05",
      "role": "user",
      "registration_date": "2022-03-09T16:01:07Z"
    }
  ]
}
```

`curl -H "Accept: application/xml" http://web-04.challs.olicyber.it/users`

```xml
<?xml version="1.0"?>

<users>
  <user comment="flag{54m3_7hing_diff3r3n7_7hing}">
    <name>admin</name>
    <role>admin</role>
    <registration_date>2018-06-18T15:34:55Z</registration_date>
  </user>
  <user>
    <name>fruitfly</name>
    <role>user</role>
    <registration_date>2019-08-12T12:04:32Z</registration_date>
  </user>
  <user>
    <name>jim87</name>
    <role>user</role>
    <registration_date>2022-01-13T20:09:43Z</registration_date>
  </user>
  <user comment="Suspicious activity">
    <name>anonymous05</name>
    <role>user</role>
    <registration_date>2022-03-09T16:01:07Z</registration_date>
  </user>
</users>
```

**flag{54m3_7hing_diff3r3n7_7hing}**