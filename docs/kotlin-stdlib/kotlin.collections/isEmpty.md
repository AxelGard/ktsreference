

# isEmpty

Returns true if the array is empty.

```kotlin
inline fun <T> Array<out T>.isEmpty(): Boolean(source)
```

```kotlin
val emptyArray = arrayOf<String>()
println(emptyArray.isEmpty())   // true

val nonEmptyArray = arrayOf("Kotlin", "Java")
println(nonEmptyArray.isEmpty()) // false
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/is-empty.html)

    