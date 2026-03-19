

# also

Calls the specified function block with this value as its argument and returns this value.

```kotlin
@IgnorableReturnValueinline fun <T> T.also(block: (T) -> Unit): T(source)
```

```kotlin
val numbers = mutableListOf<Int>()
    .also { list ->
        list.add(1)
        list.add(2)
        list.add(3)
    }

println(numbers)  // Output: [1, 2, 3]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/also.html)

    