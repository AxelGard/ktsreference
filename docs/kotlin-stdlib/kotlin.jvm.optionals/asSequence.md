

# asSequence

Returns a new sequence for this Optional's value if present, or otherwise an empty sequence.

```kotlin
fun <T : Any> Optional<out T>.asSequence(): Sequence<T>(source)
```

```kotlin
import java.util.Optional
import kotlin.jvm.optionals.asSequence

fun main() {
    val present = Optional.of("Kotlin")
    present.asSequence().forEach { println(it) }

    val empty = Optional.empty<String>()
    empty.asSequence().forEach { println(it) } // nothing will be printed
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm.optionals/as-sequence.html)

    