

# toJavaUuid

Converts this kotlin.uuid.Uuid value to the corresponding java.util.UUID value.

```kotlin
@ExperimentalUuidApiinline fun Uuid.toJavaUuid(): UUID(source)
```

```kotlin
import kotlin.uuid.ExperimentalUuidApi
import kotlin.uuid.Uuid
import java.util.UUID

@OptIn(ExperimentalUuidApi::class)
fun main() {
    // Create a Kotlin UUID
    val kotlinUuid: Uuid = Uuid.random()

    // Convert it to a Java UUID
    val javaUuid: UUID = kotlinUuid.toJavaUuid()

    println("Kotlin UUID: $kotlinUuid")
    println("Java UUID:   $javaUuid")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.uuid/to-java-uuid.html)

    