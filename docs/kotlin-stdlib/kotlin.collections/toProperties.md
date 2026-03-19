

# toProperties

Converts this Map to a Properties object.

```kotlin
inline fun Map<String, String>.toProperties(): Properties(source)
```

```kotlin
import java.util.Properties

fun main() {
    val config = mapOf(
        "url" to "https://example.com",
        "timeout" to "5000",
        "debug" to "true"
    )

    val properties: Properties = config.toProperties()

    // Access a property
    println(properties.getProperty("url"))          // https://example.com
    println(properties.getProperty("timeout"))      // 5000
    println(properties.getProperty("debug"))        // true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-properties.html)

    