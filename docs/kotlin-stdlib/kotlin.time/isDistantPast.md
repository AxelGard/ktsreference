

# isDistantPast

Returns true if the instant is Instant.DISTANT_PAST or earlier.

```kotlin
val Instant.isDistantPast: Boolean(source)
```

```kotlin
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds

fun main() {
    val distantPast = Instant.DISTANT_PAST
    val veryEarly = distantPast.minus(10.seconds)

    println("Is DISTANT_PAST distant? ${distantPast.isDistantPast}")   // true
    println("Is veryEarly distant? ${veryEarly.isDistantPast}")       // true

    val now = Instant.now()
    println("Is now distant? ${now.isDistantPast}")                    // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/is-distant-past.html)

    