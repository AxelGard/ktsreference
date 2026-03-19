

# contains

Returns true if this range contains the specified element.

```kotlin
inline operator fun IntRange.contains(element: Int?): Boolean(source)
```

```kotlin
fun main() {
    val range = 1..10

    val a: Int? = 7
    val b: Int? = 15
    val c: Int? = null

    println(a in range) // true
    println(b in range) // false
    println(c in range) // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/contains.html)

    