

# getOrElse

Returns an element at the given index or the result of calling the defaultValue function if the index is out of bounds of this array.

```kotlin
inline fun <T> Array<out T>.getOrElse(index: Int, defaultValue: (Int) -> T): T(source)
```

```kotlin
val numbers = arrayOf(10, 20, 30)

// Index 5 is out of bounds, so the lambda is executed
val result = numbers.getOrElse(5) { index -> index * 2 } // result == 10

println(result)  // prints 10
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/get-or-else.html)

    