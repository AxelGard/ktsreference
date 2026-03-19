

# copy

Returns an immutable copy of this map entry with the same key and value.

```kotlin
@ExperimentalStdlibApifun <K, V> Map.Entry<K, V>.copy(): Map.Entry<K, V>(source)
```

```kotlin
import kotlin.experimental.ExperimentalStdlibApi

@OptIn(ExperimentalStdlibApi::class)
fun main() {
    val map = mapOf("foo" to 1, "bar" to 2)
    val original = map.entries.first()          // e.g. ("foo" -> 1)
    val copyEntry = original.copy()             // immutable copy of the same entry

    println("original: ${original.key}=${original.value}")
    println("copy:     ${copyEntry.key}=${copyEntry.value}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/copy.html)

    