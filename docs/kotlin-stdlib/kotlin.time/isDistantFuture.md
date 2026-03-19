

# isDistantFuture

Returns true if the instant is Instant.DISTANT_FUTURE or later.

```kotlin
val Instant.isDistantFuture: Boolean(source)
```

```kotlin
import kotlin.time.Instant

fun main() {
    val now = Instant.now()
    val distant = Instant.DISTANT_FUTURE

    println(now.isDistantFuture)          // false
    println(distant.isDistantFuture)      // true

    // A future date that is far beyond the distant future threshold
    val future = Instant.parse("9999-12-31T23:59:59.999Z")
    println(future.isDistantFuture)       // true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/is-distant-future.html)

    