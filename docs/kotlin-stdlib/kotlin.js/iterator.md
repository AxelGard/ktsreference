

# iterator

Allows to iterate this dynamic object in the following cases:

```kotlin
operator fun dynamic.iterator(): Iterator<dynamic>(source)
```

```kotlin
import kotlin.js.*

fun main() {
    val jsArray: dynamic = js("['one', 'two', 'three']")
    for (item in jsArray) {
        console.log(item)   // prints: one, two, three
    }

    val jsObject: dynamic = js("{a: 1, b: 2, c: 3}")
    for (key in jsObject) {
        console.log("$key -> ${jsObject[key]}")   // prints: a -> 1, b -> 2, c -> 3
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/iterator.html)

    