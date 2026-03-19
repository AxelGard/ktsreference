

# json

Returns a simple JavaScript object (as Json) using provided key-value pairs as names and values of its properties.

```kotlin
fun json(vararg pairs: Pair<String, Any?>): Json(source)
```

```kotlin
import kotlin.js.json

fun main() {
    val user = json(
        "id" to 123,
        "username" to "john_doe",
        "email" to "john@example.com",
        "roles" to listOf("admin", "editor")
    )
    console.log(user)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/json.html)

    