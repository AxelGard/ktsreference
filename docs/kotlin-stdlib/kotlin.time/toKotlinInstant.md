

# toKotlinInstant

Converts the JS Date to the corresponding Instant.

```kotlin
fun Date.toKotlinInstant(): Instant(source)
```

```kotlin
import kotlin.time.Instant
import kotlin.time.toKotlinInstant

fun main() {
    val jsDate = Date()                     // JS Date instance
    val instant: Instant = jsDate.toKotlinInstant()
    println("Instant: $instant")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/to-kotlin-instant.html)

    